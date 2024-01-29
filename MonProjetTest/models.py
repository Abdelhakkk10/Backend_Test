
from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomUser(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('simple-user', 'Simple User'),
    )

    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255, default="")
    role = models.CharField(max_length=15, choices=ROLES)

    objects = CustomUserManager()

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        related_query_name='user',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        related_query_name='user',
        blank=True,
        help_text='Specific permissions for this user.',
    )

    def __str__(self):
        return self.username

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.get_or_create(user=instance)

class Task(models.Model):
    PRIORITIES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    )

    STATUSES = (
        ('todo', 'To Do'),
        ('in-progress', 'In Progress'),
        ('done', 'Done'),
    )

    title = models.CharField(max_length=255)
    description =  models.TextField(blank=True, null=True)
    priority = models.CharField(max_length=10, choices=PRIORITIES)
    status = models.CharField(max_length=15, choices=STATUSES)
    last_updated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    ROLES = (
        ('admin', 'Admin'),
        ('simple-user', 'Simple User'),
    )

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    role = models.CharField(max_length=15, choices=ROLES)

    def __str__(self):
        return self.username
