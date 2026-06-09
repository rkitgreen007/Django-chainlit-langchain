# myproject/models.py
from django.db import models

class Order(models.Model):
    order_id = models.CharField(max_length=50, unique=True)
    customer_name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default="Processing")
    items = models.TextField()

    def __str__(self):
        return f"Order {self.order_id} - {self.status}"
