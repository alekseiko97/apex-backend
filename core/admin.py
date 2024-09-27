from django.contrib import admin
from .models import Organization, Category, Product, UserProfile

admin.site.register(Organization)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(UserProfile)
