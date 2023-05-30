from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator, MaxLengthValidator
from accounts.models import GardenOwnerProfile


class Garden(models.Model):
    garden_owner = models.OneToOneField(GardenOwnerProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    business_code = models.CharField(max_length=12, validators=[MinLengthValidator(12)])
    address = models.TextField()
    avg_score = models.FloatField(default=0.0, validators=[MinValueValidator(0.0), MaxValueValidator(5.0)])
    location = models.URLField(null=True, blank=True)
    profile_photo = models.ImageField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name
