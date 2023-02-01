
from django.urls import path
from store import views


urlpatterns = [
    path('', views.store, name='store'),
    # angle bracket: to capture part of the URL and send it as a keyword argument to the view.
    # The angle brackets may include a converter specification (like the one below)
    # which limits the characters matched and may also change the type of the variable passed to the view
    path('<slug:category_slug>/', views.store, name = 'product_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail')
]
