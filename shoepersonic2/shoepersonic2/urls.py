"""shoepersonic2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import index
from accounts import urls as account_urls 
from django.urls import path, re_path, include
from django.conf import settings
from shop import urls as shop_urls
from basket import urls as basket_urls
from checkout import urls as checkout_urls
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('accounts/', include(account_urls)),
    path('shop/', include(shop_urls)),
    path('basket/', include(basket_urls)),
    path('checkout/', include(checkout_urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
