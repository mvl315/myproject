from django.shortcuts import render

def index(request):
    return render(request, "main/index.html")

def page(request):
    return render(request, "main/page.html")

def about(request):
    return render(request, "main/about.html")

def contracts(request):
    return render(request, "main/contracts.html")

def custom(request):
    return render(request, "main/custom.html")

def profile(request):
    return render(request, "main/profile.html")

def registr(request):
    return render(request, "main/registr.html")
