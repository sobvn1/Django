from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books_views, name='books'),
    path('books_detail/<int:id>/', views.books_detail, name='detail'),
    path('books/<int:id>/uptade/', views.uptade_books_view, name='uptade'),
    path('books/<int:id>/delete/', views.delete_books_view, name='delete'),
    path('add_books/', views.add_books_view, name='create_books'),
]
