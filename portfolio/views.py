from django.http import HttpResponse
from django.shortcuts import render

# index = lambda request: render(request, 'portfolio/index.html')
def index(request):
    return render(request, 'portfolio/index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")