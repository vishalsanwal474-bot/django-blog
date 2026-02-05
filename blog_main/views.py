
# from django.http import HttpResponse- 01
from django.shortcuts import render



def home(request):
    # return HttpResponse('<h2>Homepage</h2>')- 01
    return render(request, 'home.html')