from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("library", views.library, name="library"),
    path("forum", views.forum, name="forum"),
    path("my_reviews", views.my_reviews, name="my_reviews"),
    path("post_review", views.post_review, name="post_review"),
    path("library/<int:pk>", views.wine_detail, name="wine_detail"),
]