from django.shortcuts import render


def about_api(request):
    return render(request, "paintball/about_api.html")

def model_page(request):
    return render(request, "paintball/model.html")

def making_of(request):
    return render(request, "paintball/making_of.html")