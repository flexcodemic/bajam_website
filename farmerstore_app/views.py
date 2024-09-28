from django.shortcuts import render

def home(request):
    return render(request, 'farmerstore_app/home.html') # Render the homepage template
