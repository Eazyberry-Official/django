from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.TextField(default="")
    description = models.TextField(default="")
    price = models.TextField(default="")
    summary = models.TextField(default="Default test")