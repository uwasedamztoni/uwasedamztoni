
from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category
from carts.models import CartItem
from django.db.models import Q
from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse

def store(request, category_slug=None):
    print("Category Slug Received:", category_slug)  # Debugging line

    products = None
    paged_products = None
    product_count = 0

    if category_slug:
        # Retrieve the category by slug
        category = get_object_or_404(Category, slug=category_slug)
        # Filter products by the selected category
        products = Product.objects.filter(category=category, is_available=True)
        paginator = Paginator(products, 2)  # Use a lowercase variable name for the instance
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)  # Corrected instance access to get_page
        product_count = products.count()
    else:
        # If no category_slug, display all products
        products = Product.objects.filter(is_available=True).order_by('id')
        # Create a paginator instance and paginate products with 6 items per page
        paginator = Paginator(products, 4)  # Use a lowercase variable name for the instance
        page = request.GET.get('page')
        paged_products = paginator.get_page(page)  # Corrected instance access to get_page
        product_count = products.count()

    context = {
        'products': paged_products if paged_products else products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        in_cart = CartItem.objects.filter(cart__cart_id=_cart_id(request), product=single_product).exists()
       
    except Exception as e:
        raise e  # Properly indented

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
    }
    return render(request, 'store/product_detail.html', context)


def search(request):
    products = []
    product_count = 0  # Initialize product_count

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            # Corrected 'created_date' and 'description__icontains'
            products = Product.objects.order_by('created_date').filter(
                Q(description__icontains=keyword) | Q(product_name__icontains=keyword)
            )
            product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count,
    }
    
    return render(request, 'store/store.html', context)


