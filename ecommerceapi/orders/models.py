from django.db import models
from users.models import CustomerProfile


class Orders(models.Model):
    order_name = models.CharField(max_length=200, null=True, blank=True)
    customer = models.ForeignKey(
        CustomerProfile, on_delete=models.CASCADE, null=True, related_name="customer",)

    def __str__(self):
        return self.order_name
