from django.contrib import admin
from .models import Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name', 'slug',)




# The register function is used to add models to the Django admin so that data for those models can be
# created, deleted, updated and queried through the user interface.
admin.site.register(Category, CategoryAdmin)
