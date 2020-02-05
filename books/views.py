from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, permissions
from django.shortcuts import render


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [
        permissions.IsAdminUser,
        permissions.IsAuthenticated
    ]

    serializer_class = BookSerializer

    def get_queryset(self):
        return self.request.user.books.all()
