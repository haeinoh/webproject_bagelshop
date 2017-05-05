from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'register',views.register, name='register'),
    url(r'menu',views.products, name='products'),
    url(r'custom_recipe',views.custom, name='custom'),
    url(r'custom_recipe/new', views.custom_new, name='custom_new'),
    url(r'order',views.orders,name='orders'),
    url(r'cart',views.cart,name='cart'),
]
