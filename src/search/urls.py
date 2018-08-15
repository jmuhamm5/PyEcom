from django.urls import path

from .views import SearchProductListView

app_name = "search" # django 2 feature for namespace to work in main url file

urlpatterns = [
    path('', SearchProductListView.as_view(), name='list')
] 