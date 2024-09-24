from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=255)

class User(models.Model):
    email = models.EmailField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category)