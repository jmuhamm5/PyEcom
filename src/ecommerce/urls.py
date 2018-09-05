from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from accounts.views import login_page, register_page
from .views import home_page, about_page, contact_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls', namespace='products')),
    path('search/', include('search.urls', namespace='search')),
    path('cart/', include('carts.urls', namespace='cart')),
    path('', home_page, name='home'),
    path('about/', about_page, name='about'),
    path('contact/', contact_page, name='contact'),
    path('login/', login_page, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register_page, name='register')
] 

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
