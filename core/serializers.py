from rest_framework import serializers
from .models import Organization, Product, Category, User

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'ean', 'sku', 'url']
    
# categories    
class CategoryOverviewSerializer(serializers.ModelSerializer):
    products_count = serializers.IntegerField(read_only=True)  # Add products count
    subcategories = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'is_active', 'created_at', 'subcategories', 'products_count']  # Only products_count here

    def get_subcategories(self, obj):
        subcategories = obj.subcategories.all()
        return CategoryOverviewSerializer(subcategories, many=True).data

class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)  # Include full product details

    class Meta:
        model = Category
        fields = ['id', 'name', 'is_active', 'created_at', 'products']  # Include the full product set
    
class UserSerializer(serializers.ModelSerializer):
    organization = serializers.PrimaryKeyRelatedField(queryset=Organization.objects.all())

    class Meta:
        model = User
        fields = ['id', 'organization']