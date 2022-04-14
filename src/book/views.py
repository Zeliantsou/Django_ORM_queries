
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action

from book.models import Author, Publisher, Book, Sales
from book.services import (
    get_authors_whose_book_name_not_exist_symbol_A,
    get_count_books_each_author,
    get_authors_with_count_books_more_five,
    get_author_publisher_without_ids,
    get_birth_year_oldest_author,
    get_authors_by_raw_sql,
    get_birth_year_in_16_or_18_century,
    get_the_most_reach_publisher,
    get_count_books_publish_date_after_2000,
    get_latest_published_book_by_two_ways,
    get_one_book_for_each_year,
    get_book_with_publishers_without_other_fields,
    service_check_if_book_id_eq_100_exists,
    service_create_book_if_not_exist_name,
    generate_books_data,
    create_five_books,
)


class AuthorViewSet(GenericViewSet):
    """View set for Author model"""
    queryset = Author.objects.all()

    @action(detail=False, methods=('get',))
    def authors_whose_book_name_not_exist_symbol_A(self, request):
        response_data = get_authors_whose_book_name_not_exist_symbol_A()
        return Response(status=HTTP_200_OK, data=response_data)

    @action(detail=False, methods=('get',))
    def count_books_each_author(self, request):
        response_data = get_count_books_each_author()
        return Response(status=HTTP_200_OK, data=response_data)

    @action(detail=False, methods=('get',))
    def authors_with_count_books_more_five(self, request):
        response_data = get_authors_with_count_books_more_five()
        return Response(status=HTTP_200_OK, data=response_data)

    @action(detail=False, methods=('get',))
    def author_publisher_without_ids(self, request):
        response_data = get_author_publisher_without_ids()
        return Response(status=HTTP_200_OK, data=response_data)

    @action(detail=False, methods=('get',))
    def birth_year_oldest_author(self, request):
        response_data = get_birth_year_oldest_author()
        return Response(status=HTTP_200_OK, data=response_data)

    @action(detail=False, methods=('get',))
    def authors_by_raw_sql(self, request):
        response_data = get_authors_by_raw_sql()
        return Response(status=HTTP_200_OK, data=response_data)


class PublisherViewSet(GenericViewSet):
    """View set for Publisher model"""
    queryset = Publisher.objects.all()

    @action(detail=False, methods=('get',))
    def birth_year_in_16_or_18_century(self, request):
        response_data = get_birth_year_in_16_or_18_century()
        return Response(status=HTTP_200_OK, data=response_data)

    @action(detail=False, methods=('get',))
    def the_most_reach_publisher(self, request):
        response_data = get_the_most_reach_publisher()
        return Response(status=HTTP_200_OK, data=response_data)


class BookViewSet(GenericViewSet):
    """View set for Book model"""
    queryset = Book.objects.all()

    @action(detail=False, methods=('get',))
    def count_books_publish_date_after_2000(self, request):
        response_data = get_count_books_publish_date_after_2000()
        return Response(status=HTTP_200_OK, data=response_data)

    @action(detail=False, methods=('get',))
    def latest_published_book_by_two_ways(self, request):
        response_data = get_latest_published_book_by_two_ways()
        return Response(status=HTTP_200_OK, data=response_data)

    @action(detail=False, methods=('get',))
    def one_book_for_each_year(self, request):
        response_data = get_one_book_for_each_year()
        return Response(status=HTTP_200_OK, data=response_data)

    @action(detail=False, methods=('get',))
    def book_with_publishers_without_other_fields(self, request):
        response_data = get_book_with_publishers_without_other_fields()
        return Response(status=HTTP_200_OK, data=response_data)

    @action(detail=False, methods=('get',))
    def check_if_book_id_eq_100_exists(self, request):
        response_data = service_check_if_book_id_eq_100_exists()
        return Response(status=HTTP_200_OK, data=response_data)

    @action(detail=False, methods=('get',))
    def create_book_if_not_exist_name(self, request):
        response_data = service_create_book_if_not_exist_name()
        return Response(status=HTTP_200_OK, data=response_data)

    @action(detail=False, methods=('get',))
    def price_above_20_february_2002(self, request):
        pass

    @action(detail=False, methods=('post',))
    def create_five_books_by_one_query(self, request):
        five_books_data = generate_books_data()
        create_five_books(five_books_data)
        response_data = "Five random books were created"
        return Response(status=HTTP_200_OK, data=response_data)


class SalesViewSet(GenericViewSet):
    """View set for Sales model"""
    queryset = Sales.objects.all()
