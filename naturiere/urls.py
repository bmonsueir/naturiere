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
from django.conf.urls import url, include
from django.contrib import admin
# from analyze import urls
# from blog import urls
from consumer import urls
# from products import urls

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^analyze/', include('analyze.views')),
    # url(r'^blog/', include('blog.views')),
    url(r'^consumer/', include('consumer.views')),
    # url(r'^products/', include('products.views')),
    url(r'^$','index', name ='index')
]
