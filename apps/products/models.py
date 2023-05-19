from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from ..customers.models import CustomUser


class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,  blank=True, null=True)