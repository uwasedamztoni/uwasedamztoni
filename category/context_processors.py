from .models import Category

def menu_links(request):
    links = Category.objects.all()  # Corrected variable name
    return {'links': links}
