from django.shortcuts import render

from . import models
def books_views(request):
    show = models.TvShow.objects.all()
    return render(request, 'books_show.html', {'show_objects': show})

def books_detail(request, id):
    show_detail = get_object_or_404(models.BOOKS, id=id)
    return render(request, 'books_detail.html', {'object_detail': show_detail})
