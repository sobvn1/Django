from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.books_views, name='tv_show'),
    path('books_detail/<int:id>/', views.books_detail, name='detail')
]