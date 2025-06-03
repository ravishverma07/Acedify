from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import SEMESTER_CHOICES


class CustomUser(AbstractUser):
    """Custom user model extending Django's AbstractUser."""
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    semester = models.CharField(max_length=4, 
                                choices=SEMESTER_CHOICES,
                                null=True, 
                                blank=True, 
                                default='none',
                                help_text="Select your current semester")
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.username  
