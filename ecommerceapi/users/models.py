from django.db import models
from django.contrib.auth.models import User


class CustomerProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    mobile_no = models.CharField(max_length=50)
    town = models.CharField(max_length=200, null=True, blank=True)
    is_active = models.BooleanField(default=False)
