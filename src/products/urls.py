from django.urls import path

from .views import(
    ProductListView,
    ProductDetailSlugView,
) 

app_name = "products" # django 2 feature for namespace to work in main url file

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('<slug:slug>/', ProductDetailSlugView.as_view(), name='detail')
] 

