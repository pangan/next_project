from django.shortcuts import render
from django.views.decorators.cache import never_cache

@never_cache
def index(request):
    response = render(request, 'first_page/index.html')
    return response
