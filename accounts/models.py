from django.db import models
from django.contrib.auth.models import User
from base.models import *
from phonenumber_field.modelfields import PhoneNumberField

class MemberProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    directorate = models.ForeignKey(
        Directorate,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='members'
    )
    phone_number = PhoneNumberField(region='KE', blank=True)

    def __str__(self):
        return self.user.username if self.user else "Deleted User"
