from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books_views, name='books'),
    path('books_detail/<int:id>/', views.books_detail, name='detail')
]