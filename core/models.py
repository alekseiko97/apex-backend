from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'organization' 

class User(models.Model):
    email = models.EmailField()
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    class Meta:
        db_table = 'user' 

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    class Meta:
        db_table = 'category' 

class Product(models.Model):
    name = models.CharField(max_length=255)
    categories = models.ManyToManyField(Category)

    class Meta:
        db_table = 'product' 