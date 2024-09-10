from django.db import models

# Create your models here.
class Baby(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField()
    Password=models.CharField(max_length=8)
    ConfirmPassword=models.CharField(max_length=8)

