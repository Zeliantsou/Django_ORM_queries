from django.contrib import admin

from book.models import Author, Publisher, Book, Sales


class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'birth_day',
    )


class PublisherAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'publisher',
        'publish_date',
        'price',
    )


class SalesAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'date',
        'total_sold_usd',
    )


admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Sales, SalesAdmin)
