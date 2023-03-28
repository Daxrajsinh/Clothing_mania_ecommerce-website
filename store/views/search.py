from django.views import View
from store.models.product import Products
from django.shortcuts import render

class SearchView (View):
    def get(self, request):
        query = request.GET.get('q')
        products = Products.objects.filter(name__icontains=query)
        context = {
            'query': query,
            'products': products
        }
        return render(request, 'search.html', context)