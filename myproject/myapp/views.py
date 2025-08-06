from django.shortcuts import render
def home(request):
    return render(request, 'home.html')
# Create your views here.
def category(request):
    return render(request, 'category.html')

def cart(request):
    return render(request, 'cart.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def profile(request):
    return render(request, 'profile.html')

def exterior(request):
    return render(request, 'categories/exterior.html')