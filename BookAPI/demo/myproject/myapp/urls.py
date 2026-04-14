from django.urls import path
from . import views

urlpatterns = [
    path('book/', views.book),
    path('menu/', views.menu),
    path('booklist/', views.BookList.as_view()),
    path('bookmenu/', views.BookMenuView.as_view()),
    path('bookmenu/<int:pk>/', views.SingleBookMenuView.as_view()),
]