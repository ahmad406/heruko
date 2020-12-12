from django.db import models
from django.contrib.auth.models import User


class extenduser(models.Model):
    phone = models.IntegerField()
    address = models.TextField(max_length=100)
    state =models.CharField(max_length=10)
    city =  models.CharField(max_length=10)
    pin_code = models.IntegerField()
    user = models.OneToOneField(User,on_delete =models.CASCADE)

    def __str__(self):
        return str(self.user)