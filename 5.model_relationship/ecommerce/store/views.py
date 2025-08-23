from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Order

def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    return render(request, "store/home.html", {
        "products": products,
        "categories": categories
    })


def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(request, "store/category_products.html", {
        "category": category
    })


def order_summary(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    # No need to fetch all products, use order.products.all in template
    return render(request, "store/order_summary.html", {
        "order": order
    })
