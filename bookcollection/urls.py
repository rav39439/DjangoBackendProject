

from django.contrib import admin
from django.urls import path
from bookcollection import views

urlpatterns = [
    path('', views.index,name="home"),
    path('contact/', views.contact,name="contact"),

    path('test/', views.test,name="test"),
    path('AddBook', views.addBook,name="addbook"),
    path('getBook', views.getBook,name="getBook"),
    path('getBookbyId/<int:id>', views.getBookbyId,name="getBookbyId"),

    path('getReview/<int:id>', views.getReviews,name="getReviews"),
    path('register', views.register,name="register"),
    path('login', views.login,name="login"),

    path('AddReview/<int:id>', views.addReviews,name="addReviews"),
    path('editReview/<int:id>', views.addReviews,name="addReviews"),

]
