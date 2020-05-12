from django.db import models

# Create your models here.


class Product(models.Model):
    # Clase default de django
    title = models.TextField()
    # Tipo de dato texto
    description = models.TextField()
    price = models.TextField()
    summary = models.TextField(default='this is cool!')
