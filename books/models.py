from django.db import models


class BOOKS(models.Model):
    GENRE = (
        ('Roman', 'Роман'),
        ('Detective', 'Детектив'),
        ('Horror', 'Хоррор'),
        ('Manga', 'Манга'),
        ('Comedy', 'Комедия'),
        ('Fantastic', 'Фантастика')
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    genre = models.CharField(max_length=100, choices=GENRE)
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

