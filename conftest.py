import pytest

from main import BooksCollector


@pytest.fixture
def books():
    books = BooksCollector()
    books.books_genre = {
        'Дюна': 'Фантастика',
        'Меч предназначения': '',
        'Сияние': 'Ужасы',
        'Гарри Поттер и узник Азкабана': '',
        'Хоббит, или туда и обратно': 'Фантастика',
        'Вокруг света за 80 дней': 'Фантастика'
    }

    books.favorites = ['Дюна', 'Хоббит, или туда и обратно']
    return books
