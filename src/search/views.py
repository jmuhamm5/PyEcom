from django.shortcuts import render
from django.views.generic.list import ListView
from products.models import Product

# Create your views here.

class SearchProductListView(ListView):
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductListView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None) # mod_dict['q']
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.featured()

        '''
        __icontains = field contains this
        __iexact = field is exactly this
        '''