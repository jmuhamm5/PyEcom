from django.urls import path

from .views import cart_home

app_name = "cart" # django 2 feature for namespace to work in main url file

urlpatterns = [
    path('', cart_home, name='cart')
] 