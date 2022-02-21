from django.urls import path
from django.urls.resolvers import URLPattern
from .views import (
    product_create_view,
    product_detail_view,
    product_delete_view,
    product_list_view,
    render_initial_data,
    dynamic_lookup_view,
)

app_name = 'products' # needed to refer to this particual sub-urls.py
urlpatterns = [
    path('product/', product_detail_view),
    path('create/', product_create_view),
    path('initial/', render_initial_data),
    path('<int:id>/', dynamic_lookup_view, name='product'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
    path('', product_list_view, name='product-list'),
]

# In the beginning we had all urls in the base urls.py but it's more modular and better to have them
# divided into a urls.py for each module. That way if two paths/views have the same name, we will search in the module first
# and if not found we will go to the up the chain and look