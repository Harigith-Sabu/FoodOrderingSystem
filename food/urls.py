"""food URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from app import views
from django.contrib.auth import views as auth
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('log/',views.log,name='log'),
    path('logout',auth.LogoutView.as_view(template_name='home.html'),name='logout'),
    path('cat/<int:a>',views.cat,name='cat'),
    path('cart/<int:x>/',views.cart,name='cart'),
    path('search',views.search,name='search'),
    path('add_cart/<int:product_id>/',views.add_cart,name='add_cart'),
    path('cart_details',views.cart_details,name='cart_details'),
    path('remove/<int:product_id>/',views.cart_delete,name='remove'),
    path('cart_decrement/<int:product_id>/',views.min_cart,name='cart_decrement'),
    # path('ship/<int:t>/',views.ship,name='ship'),
    path('pay/<int:t>/',views.pay,name='pay'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

