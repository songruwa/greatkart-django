from django.db import models
from category.models import Category
from django.urls import reverse


# Create your models here.

class Product(models.Model):
    product_name    = models.CharField(max_length = 200, unique = True)
    slug            = models.SlugField(max_length = 200, unique = True)
    description     = models.TextField(max_length = 500, blank = True)
    price           = models.IntegerField()
    Images          = models.ImageField(upload_to = 'photos/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default = True)
    # on delete here
    # to specify whether you want rows deleted in a child table when corresponding rows are deleted in the parent table
    category        = models.ForeignKey(Category, on_delete = models.CASCADE)
    # set the timezone.now() only when the instance is created
    created_date    = models.DateTimeField(auto_now_add = True)
    # the auto_now will update the field every time the save method is called.
    modified_date  = models.DateTimeField(auto_now = True)

    def get_url(self):
        return reverse('product_detail', args = [self.category.slug, self.slug])
        # here category is a foreign key
        # thus, it refers to the slug attribute in Category model in category folder

    def __str__(self):
        return self.product_name
