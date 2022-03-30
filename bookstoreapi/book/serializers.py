from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from book.models import Book

class BookSerializer(ModelSerializer):
    class Meta:
        model=Book
        fields=["book_name","author","price","copies"]
        