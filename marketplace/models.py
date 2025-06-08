from django.db import models
from users.models import CustomUser
from main.models import SEMESTER_CHOICES

class Item(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_posted = models.DateField(auto_now_add=True)
    semester = models.CharField(max_length=4, choices=SEMESTER_CHOICES, null=True, blank=True, default='none')
    is_available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='listing_images', null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.user.username}"

