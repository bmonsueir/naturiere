from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.products,name='products'),
    url(r'^product/(?P<pk>\d+)$', views.product, name='product'),
]