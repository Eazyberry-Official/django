from django.db import models

class user_uploads(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(default="")
    price = models.DecimalField(max_digits=11, decimal_places = 4)
    image = models.ImageField(upload_to='products/', default= "products/chairman.png")