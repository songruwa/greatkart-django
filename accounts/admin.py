from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.

# making custom password field read-only
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active', )
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',) # show in descending order

    # a ManyToManyField is displayed in the admin site with a <select multiple>.
    filter_horizontal = ()
    # ModelAdmin classes can define list filters that appear in the right sidebar of the change list page of the admin
    list_filter = ()
    # Set fieldsets to control the layout of admin “add” and “change” pages.
    fieldsets = () # make the password read-only



admin.site.register(Account, AccountAdmin)
