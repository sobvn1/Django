from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models, forms
def books_views(request):
    show = models.BOOKS.objects.all()
    return render(request, 'books_show.html', {'show_objects': show})

def books_detail(request, id):
    show_detail = get_object_or_404(models.BOOKS, id=id)
    return render(request, 'books_detail.html', {'object_detail': show_detail})
def add_books_view(request):
    method = request.method
    if method == 'POST':
        form = forms.ShowForm(request.POST, request.FILES)
        form.save()
        return HttpResponse('<h1>Книга успешно добавлен</h1>')
    else:
        form = forms.ShowForm()

    return render(request, 'create_books.html', {'form': form})
def uptade_books_view(request, id):
    show_object = get_object_or_404(models.BOOKS, id=id)
    if request.method == 'POST':
        form = forms.ShowForm(instance=show_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1> Фильм успешно обновлен <h1/>')
    else:
        form = forms.ShowForm(instance=show_object)
        return render(request, 'books_uptade.html', {'form': form, 'object': show_object})
def delete_books_view(request, id):
    show_object = get_object_or_404(models.BOOKS, id=id)
    show_object.delete()
    return  HttpResponse('<h1>Книга успешно удалена<h1/>')