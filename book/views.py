from django.shortcuts import render

from . import models

def blogview(request):
    book = models.Book.objects.all()
    return render(request, 'book.html', {'book': book})