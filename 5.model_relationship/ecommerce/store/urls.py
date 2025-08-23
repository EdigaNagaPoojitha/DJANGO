from .views import home, category_products, order_summary
from django.urls import path

urlpatterns = [
    path('', home, name="home"),
    path('category/<int:category_id>/', category_products, name="category_products"),
    path('order/<int:order_id>/', order_summary, name="order_summary"),
]