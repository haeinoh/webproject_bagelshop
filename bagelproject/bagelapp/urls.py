from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'register',views.register, name='register'),
    url(r'menu',views.product, name='menu_post'),
    url(r'custom_recipe',views.custom_post, name='custom_recipe'),
    url(r'order',views.order,name='order_post'),
    url(r'show',views.show, name='show'),
    url(r'add',views.add, name='add'),
    url(r'remove',views.remove, name='remove'),
]
