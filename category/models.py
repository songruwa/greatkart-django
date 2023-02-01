from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length = 50, unique = True)
    # slug: unique identifying part of a web address, typically at the end of the URL
    slug = models.SlugField(max_length = 100, unique = True)
    description = models.CharField(max_length = 255, blank = True)
    cat_image = models.ImageField(upload_to = 'photo/categories', blank = True) # upload: defines a path when we upload an image where we should store this image

    # Model Meta is basically used to change the behavior of your model fields like changing order options
    # ,verbose_name, and a lot of other options.
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    # this function will bring us the url of the matching category
    def get_url(self):
        # the reverse function allows to retrieve url details from url’s.py file through the name value provided there.
        # This looks through all URLs defined in your project for the URL defined with the name 'product_by_category'
        return reverse('product_by_category', args=[self.slug])
        # args: allows us to pass a variable number of non-keyword arguments to a Python function

    # make a string representation of this model
    # purpose:
    # return a human-readable string for each object
    # to display an object in the Django admin site and as the value inserted into a template when it displays an object.
    def __str__(self):
        return self.category_name
