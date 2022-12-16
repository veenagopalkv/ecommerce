from django.urls import path
from . import views
app_name='cartApp'
urlpatterns=[
    path("add/<int:product_id>/",views.add_to_cart,name='add_to_cart'),
    path("",views.cart_details,name='cart_details'),
    path("remove/<int:product_id>/",views.cart_remove,name='cart_remove'),
    path("fullremove/<int:product_id>/", views.full_remove, name='full_remove')

]
