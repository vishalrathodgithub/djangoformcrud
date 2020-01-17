from django.db import models


# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    page = models.PositiveIntegerField()
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.book_name

    class Meta:
        managed = True
        db_table = 'book_table'
