from django.shortcuts import render
from rest_framework.response import Response
from book.serializers import BookSerializer
from book.models import Book
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from book import serializers

class Books(APIView):
    def get(self,request):
        books=Book.objects.all()
        serializers=BookSerializer(books,many=True)
        return Response(serializers.data)

    def post(self,request):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class BooksDetails(APIView):
    def get_object(self,id):
        try:
            return Book.objects.get(id=id)
        except Book.DoesNotExist:
            raise Http404


    def get(self,request,*args,**kwargs):
        id=kwargs["id"]
        book=self.get_object(id)
        serializer=BookSerializer(book)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,*args,**kwargs):
        id=kwargs["id"]
        book=self.get_object(id)
        serializer=BookSerializer(book,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,*args,**kwargs):
        book=self.get_object(kwargs["id"])
        book.delete()
        return Response(status=status.HTTP_200_OK) 