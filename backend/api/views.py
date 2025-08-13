from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth import authenticate
from core.models import User, BusinessUser
from .serializers import RegisterSerializer, UserSerializer
from django.shortcuts import get_object_or_404
import re

@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User registered successfully."})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, email=email, password=password)
    if user is not None:
        return Response({"token": "fake-token", "current_role": user.current_role, "email": user.email})
    return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def swap_role(request):
    user = request.user
    new_role = request.data.get('role')
    # Define allowed roles
    allowed_roles = ['client', 'business']
    if not new_role or new_role not in allowed_roles:
        return Response({"error": "Invalid or missing role"}, status=status.HTTP_400_BAD_REQUEST)
    user_name = re.sub(r'^_{1,2}', '', user.username, count=1) 
    try:
        base_user = get_object_or_404(User, username=user_name)
    except:
        return Response({"Message": "Client user not found"}, status=status.HTTP_404_NOT_FOUND)
    # Store role in LastRole table
    LastRole.objects.update_or_create(
        user=base_user,
        defaults={'role': 'BUSINESS' if new_role == 'business' else 'CLIENT'}
    )

    # Switch username logic to mimic Authentication endpoint
    if new_role == 'business':
        switched_username = f"__{base_user.username}"
    else:
        switched_username = base_user.username
    switched_email = base_user.email if new_role != 'business' else f"bus__{user.email}"
    switched_user, created = User.objects.get_or_create(
        username=switched_username,
        defaults={
            'email': switched_email,
            'password': 'TemporaryPass123!',  # dummy password
            'current_role': new_role
        }
    )
         # Create profile entry if needed
    if new_role == 'business':
            BusinessUser.objects.get_or_create(user=switched_user)
    else:
            ClientUser.objects.get_or_create(user=switched_user)

    # Make sure current_role is updated
    switched_user.current_role = new_role
    switched_user.save()

    # Create or get token
    token, _ = Token.objects.get_or_create(user=switched_user)

    # Return same style response
    return Response({
        'token': token.key,
        'user_id': switched_user.id,
        'email': switched_user.email,
        'role': switched_user.current_role
    }, status=status.HTTP_200_OK)



from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from core.models import User, LastRole

from core.models import BusinessUser, ClientUser

class Authentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        base_user = serializer.validated_data['user']

        last_role, _ = LastRole.objects.get_or_create(
            user=base_user,
            defaults={'role': 'CLIENT'}
        )

        role = last_role.role
        if role == 'BUSINESS':
            switched_username = f"__{base_user.username}"
        else:
            switched_username = base_user.username

        switched_email = base_user.email if role != 'BUSINESS' else f"bus__{base_user.email}"

        switched_user, created = User.objects.get_or_create(
            username=switched_username,
            defaults={
                'email': switched_email,
                'password': 'TemporaryPass123!',
                'current_role': 'Business' if role == 'BUSINESS' else 'Client'
            }
        )

        # Create profile entry if needed
        if role == 'BUSINESS':
            BusinessUser.objects.get_or_create(user=switched_user)
        else:
            ClientUser.objects.get_or_create(user=switched_user)


        token, _ = Token.objects.get_or_create(user=switched_user)

        return Response({
            'token': token.key,
            'user_id': switched_user.id,
            'email': switched_user.email,
            'role': switched_user.current_role
        }, status=status.HTTP_200_OK)

