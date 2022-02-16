from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.mixins import (
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
)

from book.models import Author, Publisher, Book, Sales


class AuthorViewSet(CreateModelMixin,
                    RetrieveModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin,
                    ListModelMixin,
                    GenericViewSet):
    """View set for Author model"""
    queryset = Author.objects.all()


class PublisherViewSet(CreateModelMixin,
                    RetrieveModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin,
                    ListModelMixin,
                    GenericViewSet):
    """View set for Publisher model"""
    queryset = Publisher.objects.all()


class BookViewSet(CreateModelMixin,
                    RetrieveModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin,
                    ListModelMixin,
                    GenericViewSet):
    """View set for Book model"""
    queryset = Book.objects.all()


class SalesViewSet(CreateModelMixin,
                    RetrieveModelMixin,
                    UpdateModelMixin,
                    DestroyModelMixin,
                    ListModelMixin,
                    GenericViewSet):
    """View set for Sales model"""
    queryset = Sales.objects.all()
