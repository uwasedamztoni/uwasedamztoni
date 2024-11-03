from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category

def store(request, category_slug=None):
    print("Category Slug Received:", category_slug)  # Debugging line

    products = None
    product_count = 0

    if category_slug:
        # Retrieve the category by slug
        category = get_object_or_404(Category, slug=category_slug)
        # Filter products by the selected category
        products = Product.objects.filter(category=category, is_available=True)
        product_count = products.count()
    else:
        # If no category_slug, display all products
        products = Product.objects.filter(is_available=True)
        product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    
    return render(request, 'store/product_detail.html')

   
