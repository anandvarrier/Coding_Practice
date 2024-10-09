from django.shortcuts import render

# Create your views here.
def allChai(request):
    return render(request, 'chaiapp/all_chai.html')