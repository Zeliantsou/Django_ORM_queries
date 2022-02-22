from typing import Dict, List
import datetime

from django.db.models import Q, Count, Min, Max, Sum
from django.db.models.query import QuerySet

from book.models import Author, Publisher, Book, Sales
from initial_data.initial_test_data import create_books_data


def get_authors_whose_book_name_not_exist_symbol_A() -> QuerySet:
    return Author.objects.filter(
        ~Q(books__name__contains='A')).values('name')


def get_count_books_each_author() -> QuerySet:
    return Author.objects.annotate(
        count_books=Count('books')).values('name', 'count_books')


def get_authors_with_count_books_more_five() -> QuerySet:
    return Author.objects.alias(
        count_books=Count('books')).filter(
        count_books__gt=5).values('name')


def get_author_publisher_without_ids() -> Dict:
    return Author.objects.prefetch_related(
        'books__name').all().values('name', 'books__name')


def get_birth_year_oldest_author() -> str:
    year_of_birth_oldest_author = Author.objects.aggregate(
        Min('birth_day')).get('birth_day__min').year
    return f'the oldest author was born in {year_of_birth_oldest_author}'


def get_authors_by_raw_sql() -> List:
    authors = []
    for author in Author.objects.raw("SELECT * FROM book_author"):
        authors.append(author.name)
    return authors


def get_birth_year_in_16_or_18_century() -> QuerySet:
    return Publisher.objects.filter(
        Q(books__authors__birth_day__year__range=(1500, 1599)) |
        Q(books__authors__birth_day__year__range=(
            1700, 1799))).distinct().values('name')


def get_the_most_reach_publisher() -> Dict:
    return Publisher.objects.annotate(
        sum_books_price=Sum('books__price')).aggregate(
        Max('sum_books_price'))


def get_count_books_publish_date_after_2000() -> str:
    count_books = Book.objects.filter(
        publish_date__year__gte=2000).count()
    return f'Count books that were published after 2000: {count_books}'


def get_latest_published_book_by_two_ways() -> Dict:
    latest_published_1st_way = Book.objects.last().name
    latest_published_2nd_way = Book.objects.latest('id').name
    return {
        'latest published book first way': latest_published_1st_way,
        'latest published book second way': latest_published_2nd_way,
    }


def get_one_book_for_each_year() -> QuerySet:
    return Book.objects.all().distinct(
        'publish_date').values('name', 'publish_date')


def get_book_with_publishers_without_other_fields() -> QuerySet:
    return Book.objects.select_related(
        'publisher').all().values('name', 'publisher__name')


def service_check_if_book_id_eq_100_exists() -> str:
    book_id_100 = Book.objects.filter(id=100).exists()
    if book_id_100:
        return f"book with id=100' exists in the system"
    else:
        return "book with id=100 does not exist in the system"


def service_create_book_if_not_exist_name() -> str:
    book, created = Book.objects.get_or_create(
        name='Эйафьядлаёкюдель', defaults={
            'publisher': Publisher.objects.last(),
            'publish_date': datetime.datetime.now(),
            'price': 100
        })
    if created:
        return "book with name 'Эйафьядлаёкюдель' was created"
    else:
        return "book with name 'Эйафьядлаёкюдель' \
                already exists in the system"


def generate_books_data() -> List:
    books_list = []
    for book in create_books_data()[:5]:
        payload = book['fields']
        added_book = Book(name=payload['name'],
                          publisher=Publisher.objects.get(
                              id=payload['publisher']),
                          publish_date=datetime.datetime.strptime(
                              payload['publish_date'], '%Y-%m-%d'),
                          price=payload['price'],
                          )
        books_list.append(added_book)
    return books_list


def create_five_books(books_data: List) -> None:
    Book.objects.bulk_create(books_data)
