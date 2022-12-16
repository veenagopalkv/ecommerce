from django.urls import path
from . import views
app_name='ecommerceapp'
urlpatterns = [
    path('',views.allproductcategory,name='allproductcategory'),
    path('<slug:c_slug>/',views.allproductcategory,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>',views.productdetail,name='categoryproductdetail')
]
