from django.shortcuts import render

def home(request):
    return render(request, 'cafeteria_app/index.html')