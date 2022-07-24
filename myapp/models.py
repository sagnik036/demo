import email
from pickle import TRUE
from django.db import models
# Create your models here.
class User_Custom(models.Model):
    first_name = models.CharField(
       max_length=10,
    )
    last_name = models.CharField(
        max_length=10
    )
    profile_picture = models.ImageField(
        
    )
    username = models.CharField(
        max_length=7,
        primary_key=True
    )
    email_id = models.EmailField(
        unique=TRUE
    )
    password = models.CharField(
        max_length=8
    )
    line1 = models.CharField(
        max_length=10
    )
    city = models.CharField(
        max_length=8
    )
    state = models.CharField(
        max_length=8
    )
    pincode = models.IntegerField()


    def __str__(self):
        return self.username
