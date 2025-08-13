from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=True, null=True, unique=False)
    current_role = models.CharField(
        max_length=10,
        choices=[('client', 'Client'), ('business', 'Business')],
        default='client'
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class ClientUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='client')
    created_at = models.DateTimeField(auto_now_add=True)

class BusinessUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='business')
    created_at = models.DateTimeField(auto_now_add=True)

class LastRole(models.Model):
    ROLE_CHOICES = [('CLIENT', 'Client'), ('BUSINESS', 'Business')]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    assumed_at = models.DateTimeField(auto_now=True)  # Updated every time role changes
                
    def __str__(self):
        return f"{self.user.username} -> {self.role}"


