from django.urls import path
from .views import (
    OrganizationListCreateView,
    OrganizationDetailView,
    CategoryListCreateView,
    CategoryDetailView,
    ProductListCreateView,
    ProductDetailView,
    UserProfileListCreateView,
    UserProfileDetailView
)

urlpatterns = [
    # Organization URLs
    path('organizations/', OrganizationListCreateView.as_view(), name='organization_list_create'),
    path('organizations/<int:pk>/', OrganizationDetailView.as_view(), name='organization_detail'),

    # Category URLs
    path('categories/', CategoryListCreateView.as_view(), name='category_list_create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),

    # Product URLs
    path('products/', ProductListCreateView.as_view(), name='product_list_create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

    # UserProfile URLs
    path('userprofiles/', UserProfileListCreateView.as_view(), name='userprofile_list_create'),
    path('userprofiles/<int:pk>/', UserProfileDetailView.as_view(), name='userprofile_detail'),
]
