from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'suggestions',views.suggestions, name='suggestions'),
    url(r'register',views.register, name='register'),
    url(r'menu',views.menu,name='menu'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
