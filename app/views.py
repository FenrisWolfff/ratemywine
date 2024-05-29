from django.shortcuts import render, redirect
from .models import Wine, Rating


def home(request):
    if request.user.is_authenticated:
        return render(request, "index.html", {})
    else:
        return redirect('login')


def library(request):
    if request.user.is_authenticated:
        if request.POST:
            pass
        else:
            wine_list = Wine.objects.all()
            return render(request, "library.html", {'wine_list': wine_list})
    else:
        return redirect('login')


def forum(request):
    if request.user.is_authenticated:
        if request.POST:
            pass
        else:
            return render(request, "forum.html", {})
    else:
        return redirect('login')


def my_reviews(request):
    if request.user.is_authenticated:
        return render(request, "my_reviews.html", {})
    else:
        return redirect('login')


def post_review(request):
    if request.user.is_authenticated:
        return  render(request, "post_review.html", {})
    else:
        return redirect('login')
