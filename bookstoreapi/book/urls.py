from django.urls import path
from rest_framework import views
from book import views


urlpatterns = [
    path("books",views.Books.as_view(),name="bookall"),
    path("book/<int:id>",views.BooksDetails.as_view(),name="bookdet"),    
]