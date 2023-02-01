# purpose of this file
# Takes a request as an argument, and return the dictionary of data as a context
from .models import Category

def menu_links(request):
    # fetch all categories from the database
    links = Category.objects.all()
    return dict(links=links)
