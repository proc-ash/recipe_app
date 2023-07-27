from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class dish(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null= True, blank= True)
    dish_name = models.CharField(max_length=100, blank=False, null=False)
    dish_description = models.TextField(blank=False, null=False)
    dish_image = models.FileField(upload_to='dish_pics')

    