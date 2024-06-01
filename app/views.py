from django.shortcuts import render, redirect
from .models import Wine, Rating, Varietal, Appellation


def home(request):
    if request.user.is_authenticated:
        return render(request, "index.html", {})
    else:
        return redirect('login')


def library(request):
    if request.user.is_authenticated:
        if request.POST:
            # TODO: sorting/filtering wine list customized by user

            pass
        else:
            wine_list = Wine.objects.all()
            varietal_list = Varietal.objects.all()
            appellation_list = Appellation.objects.all()
            return render(request, "library.html", {'wine_list': wine_list,
                                                    'varietal_list': varietal_list,
                                                    'appellation_list': appellation_list})
    else:
        return redirect('login')


def wine_detail(request, pk):
    if request.user.is_authenticated:
        # TODO: add all reviews related to this wine to the page with the provided template
        return render(request, "wine_detail.html",
                      {'wine': Wine.objects.get(pk=pk)})
    else:
        return redirect('login')


def forum(request):
    if request.user.is_authenticated:
        if request.POST:
            # TODO: sorting/filtering reviews customized by user

            pass
        else:
            all_ratings = (Rating.objects.all()
                           .select_related('wine')
                           .order_by('timestamp', 'wine__wineType'))

            return render(request, "forum.html",
                          {"all_ratings": all_ratings})
    else:
        return redirect('login')


def my_reviews(request):
    if request.user.is_authenticated:
        if request.POST:
            # TODO: sorting my reviews customized by user

            pass
        else:
            # return render(request, "my_reviews.html", {})
            my_ratings = (Rating.objects.filter(user_id=request.user)
                          .select_related('wine')
                          .order_by('timestamp', 'wine__wineType'))

            return render(request, "my_reviews.html",
                          {"my_ratings": my_ratings})
    else:
        return redirect('login')


def post_review(request):
    if request.user.is_authenticated:
        if request.POST:
            # TODO: update review to database and redirect to my_reviews page
            # TODO: If review exists for the wine-user combo passed in, populate post_review.html
            #  with existing review and update existing review in the database. If review doesn't
            #  exist, create blank page and create new review in the database.

            pass
        else:
            return render(request, "post_review.html", {})
    else:
        return redirect('login')
