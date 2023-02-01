from django.shortcuts import render
from store.models import Product

def home(request):
    # first, do query
    products = Product.objects.all().filter(is_available = True)

    # A dictionary of values to add to the template context. By default, this is an empty dictionary.
    # If a value in the dictionary is callable, the view will call it just before rendering the template.
    context = {
        'products': products,
    }
    return render(request, 'home.html', context)
