from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"user/index.html")
    # return HttpResponse('hey user')