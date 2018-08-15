from django.shortcuts import render
from django.views.generic.list import ListView
from products.models import Product

# Create your views here.


class SearchProductListView(ListView):
    template_name = "products/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None) # mod_dict['q']
        print(query)
        if query is not None:
            return Product.objects.filter(title__icontains=query)
        return Product.objects.featured()

        '''
        __icontains = field contains this
        __iexact = field is exactly this
        '''