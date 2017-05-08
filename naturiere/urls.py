"""naturiere URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include, patterns
from django.contrib import admin
# from analyze import urls
from blog import urls
from customer import views
# from products import urls

urlpatterns = [
    url(r'^$',views.index, name ='index'),
    url(r'^about/',views.about, name ='about'),
    url(r'^sign_up/',views.sign_up, name ='sign_up'),
    # url(r'^admin/', admin.site.urls),
    # url(r'^analyze/', include('analyze.urls')),
    url(r'^forum/', include('blog.urls')),
    url(r'^customer/', include('customer.urls')),
    # url(r'^products/', include('products.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login_view/$', views.login_view, name='login_view'),
    url(r'^logout_view/$', views.logout_view, name='logout_view'),
]
