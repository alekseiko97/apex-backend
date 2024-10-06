from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'organization' 

class User(AbstractUser):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='users')

    class Meta:
        db_table = 'user'

# Signal to create a UserProfile when a User is created
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.userprofile.save()

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')

    class Meta:
        db_table = 'category' 
        indexes = [models.Index(fields=['name'])]  # Indexing for better performance

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default="No description available")
    sku = models.CharField(max_length=100, unique=True, null=True)  # Stock Keeping Unit
    ean = models.CharField(max_length=20, unique=True, null=True)  # European Article Number
    url = models.URLField(max_length=200, null=True)  # Link to the product page
    categories = models.ManyToManyField(Category, related_name='products')

    class Meta:
        db_table = 'product' 
        indexes = [models.Index(fields=['name'])]  # Indexing for better performance