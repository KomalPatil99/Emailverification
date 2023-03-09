from django.db import models

# Create your models here.
class Registration(models.Model):
    uname = models.CharField(max_length=50,default=None)
    email = models.EmailField()
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=255,default=None)
