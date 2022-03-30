from django.db import models


class Book(models.Model):
    book_name=models.CharField(max_length=120,unique=True)
    author=models.CharField(max_length=50)
    price=models.PositiveIntegerField(default=20)
    copies=models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.book_name