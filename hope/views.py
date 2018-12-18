from django.shortcuts import render

# Create your views here.


def index(request):
    response = render(request, 'first_page/index.html', {'amir': '4'})
    return response