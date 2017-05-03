from django.conf.urls import url
from customer import views

app_name = 'customer'

urlpatterns = [
    url(r'^$',views.customer,name='customer'),
     url(r'^about/$',views.AboutView.as_view(),name='about'),
]