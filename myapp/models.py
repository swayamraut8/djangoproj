# myapp/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models

class Lawyer(AbstractUser):
    # Custom fields for lawyers
    is_lawyer = models.BooleanField(default=True)

    # Add related_name for groups and user_permissions
    # You can use 'lawyer_groups' and 'lawyer_user_permissions' as related names
    groups = models.ManyToManyField(
        ...,
        related_name='lawyer_groups',  # Specify a unique related_name
    )
    user_permissions = models.ManyToManyField(
        ...,
        related_name='lawyer_user_permissions',  # Specify a unique related_name
    )

class Client(AbstractUser):
    # Custom fields for clients
    is_lawyer = models.BooleanField(default=False)

    # Add related_name for groups and user_permissions
    # You can use 'client_groups' and 'client_user_permissions' as related names
    groups = models.ManyToManyField(
        ...,
        related_name='client_groups',  # Specify a unique related_name
    )
    user_permissions = models.ManyToManyField(
        ...,
        related_name='client_user_permissions',  # Specify a unique related_name
    )

