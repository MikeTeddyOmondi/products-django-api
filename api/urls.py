from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    path("products/", views.products, name="products"),
    path("products/<str:pk>/", views.productDetail, name="product-detail"),
]
