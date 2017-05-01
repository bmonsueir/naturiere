from django.conf.urls import url
from customer import views

app_name = 'customer'

urlpatterns = [
    url(r'^$',views.customer,name='customer'),
]