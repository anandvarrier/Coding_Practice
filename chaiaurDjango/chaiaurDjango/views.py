from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse('Hello, you have landed on the home page of Chai aur Django')
    return render(request,template_name='index.html')

def about(request):
    # return HttpResponse('Hello, you have landed on the about page of Chai aur Django')
    return render(request, template_name='about.html')

def contact(request):
    return HttpResponse('Hello, you have landed on the contact page of Chai aur Django')