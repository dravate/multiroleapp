# urls.py

from django.urls import path, include
from rest_framework import routers
from . import views
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from rest_framework.authtoken import views as drf_views


# CSRF cookie view
@ensure_csrf_cookie
def csrf(request):
    return JsonResponse({'detail': 'CSRF cookie set'})

# DRF router setup
router = routers.DefaultRouter()
# Optional: Uncomment below if you have a viewset
# router.register(r"users", views.UserViewSet)

urlpatterns = [
    path('api/csrf/', csrf, name='csrf'),  # Sets CSRF cookie
    path('api/authentication/', views.Authentication.as_view(), name='token-auth'),
    path('api/token-test/', drf_views.obtain_auth_token),  # optional
    path('api/register/', views.register, name='register'),
    path('api/login/', views.login_view, name='login'),
    path('api/swap-role/', views.swap_role, name='swap_role'),

    # Optional: router URLs
    path('', include(router.urls)),
]

