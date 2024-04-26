
from django.db import models
from django.db import models

# Create your models here.
class Reg(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=10)
    mobile = models.CharField(max_length=11)
    dob = models.CharField(max_length=20)
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=10)
    cpassword = models.CharField(max_length=10)