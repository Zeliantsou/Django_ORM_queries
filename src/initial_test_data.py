import json
from random import uniform, randint

from barnum import gen_data


def create_authors_data():
    authors = []
    # utc = pytz.UTC
    # vr = utc.localize(vr, is_dst=None)
    for pk in range(1, 11):
        birth_day = gen_data.create_date(
            past=True,
            max_years_past=500,
            max_years_future=500).strftime('%Y-%m-%d')
        author_data = {
            "model": "book.author",
            "pk": pk,
            "fields": {
                "name": gen_data.create_name()[1],
                "birth_day": birth_day
            }
        }
        authors.append(author_data)
    return authors


def create_publishers_data():
    publishers = []
    for pk in range(1, 6):
        publisher_data = {
            "model": "book.publisher",
            "pk": pk,
            "fields": {
                "name": gen_data.create_company_name()
            }
        }
        publishers.append(publisher_data)
    return publishers


def create_books_data():
    books = []
    for pk in range(1, 100):
        book_data = {
            "model": "book.book",
            "pk": pk,
            "fields": {
                "name": gen_data.create_nouns(max=3),
                "publisher": randint(1, 6),
                "publish_date": gen_data.create_date(
                    past=True,
                    max_years_past=10,
                    max_years_future=10).strftime('%Y-%m-%d'),
                "price": round(uniform(5, 500), 2),
                "authors": list(set(randint(1, 11) for _ in range(randint(1, 3))))
            }
        }
        books.append(book_data)
    return books


def serialize_to_json(data):
    return json.dumps(data, indent=4)


def write_json_file(full_file_name, json_serializer):
    with open(full_file_name, 'w') as fp:
        fp.write(json_serializer)


def main():
    authors_data = create_authors_data()
    publishers_data = create_publishers_data()
    books_data = create_books_data()

    write_json_file('author.json', (serialize_to_json(authors_data)))
    write_json_file('publisher.json', (serialize_to_json(publishers_data)))
    write_json_file('book.json', (serialize_to_json(books_data)))


if __name__ == 'main':
    main()
