import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_default_initialisation_values_true(self):
        books_collection = BooksCollector()
        assert (
                not books_collection.books_genre
                and not books_collection.favorites
                and books_collection.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
                and books_collection.genre_age_rating == ['Ужасы', 'Детективы']
        )

    @pytest.mark.parametrize('book_name',['Дюна','Бойня номер 5, или Крестовый поход детей','t'])
    def test_add_new_book_unique_valid_name_added(self, book_name):
        books_collection = BooksCollector()
        books_collection.add_new_book(book_name)
        assert books_collection.books_genre == {book_name: ''}

    def test_add_new_book_non_unique_name_original_list_not_changed(self, books):
        expected = books.books_genre.copy()
        book_name = 'Сияние'
        books.add_new_book(book_name)
        assert books.books_genre == expected

    @pytest.mark.parametrize('book_name',['','Янки Коннектикута при дворе короля Артура', 'Странная история доктора Джекила и мистера Хайда'])
    def test_add_new_book_invalid_name_length_not_added(self, book_name):
        books_collection = BooksCollector()
        books_collection.add_new_book(book_name)
        assert book_name not in books_collection.books_genre

    @pytest.mark.parametrize(
        'book_name, book_genre',
        [
            ['Меч предназначения', 'Детективы'],
            ['Дюна', 'Фантастика'],
            ['Вокруг света за 80 дней', 'Комедии']
        ]
    )
    def test_set_book_genre_valid_data_gener_is_set(self, books, book_name, book_genre):
        books.set_book_genre(book_name, book_genre)
        assert books.books_genre[book_name] == book_genre

    @pytest.mark.parametrize(
        'book_name, book_genre',
        [
            ['Гарри Поттер и узник Азкабана', 'Фэнтези'],
            ['Властелин колец', 'Фантастика'],
            ['Цвет волшебства', 'Фэнтези'],
        ]
    )
    def test_set_book_genre_invalid_data_gener_is_not_set(self, books, book_name, book_genre):
        expected = books.books_genre.copy()
        books.set_book_genre(book_name, book_genre)
        assert books.books_genre == expected

    def test_get_book_genre_exiting_book_returns_genre(self, books):
        book_name = 'Сияние'
        books_genre = 'Ужасы'
        assert books.get_book_genre(book_name) == books_genre

    @pytest.mark.parametrize(
        'book_genre, books_in_gener',
        [
            ['Фантастика', ['Дюна', 'Хоббит, или туда и обратно', 'Вокруг света за 80 дней']],
            ['Ужасы', ['Сияние']],
            ['Мультфильмы', []]
        ]
    )
    def test_get_books_with_specific_genre_valid_genre_return_books(self, books, book_genre, books_in_gener):
        assert books.get_books_with_specific_genre(book_genre) == books_in_gener

    @pytest.mark.parametrize('book_genre',['','Фэнтези'])
    def test_get_books_with_specific_genre_invalid_genre_return_empty_list(self, books, book_genre):
        assert books.get_books_with_specific_genre(book_genre) == []

    def test_get_books_genre_return_several_items(self, books):
        expected = books.books_genre.copy()
        assert books.get_books_genre() == expected

    def test_get_books_for_children_several_children_books_return_books(self, books):
        children_books = ['Дюна','Хоббит, или туда и обратно','Вокруг света за 80 дней']
        assert books.get_books_for_children() == children_books

    def test_get_books_for_children_no_children_books_return_empty_list(self, books):
        books_collection = BooksCollector()
        books_collection.books_genre = {
            'Этюд в багровых тонах ': 'Детектив',
            'Оно': 'Ужасы',
            'Гарри Поттер и узник Азкабана': '',
        }
        assert books_collection.get_books_for_children() == []

    def test_add_book_in_favorites_existing_book_added(self,books):
        books.add_book_in_favorites('Меч предназначения')
        assert books.favorites == ['Дюна', 'Хоббит, или туда и обратно', 'Меч предназначения']

    @pytest.mark.parametrize('book_name', ['Дюна', 'Стража! Стража!'])
    def test_add_book_in_favorites_invalid_book_not_added(self, books, book_name):
        books.add_book_in_favorites(book_name)
        assert books.favorites == ['Дюна', 'Хоббит, или туда и обратно']

    def test_delete_book_from_favorites_exiting_book_removed(self, books):
        books.delete_book_from_favorites('Дюна')
        assert books.favorites == ['Хоббит, или туда и обратно']

    def test_delete_book_from_favorites_remove_non_exising_book_list_not_changed(self, books):
        books.delete_book_from_favorites('Цвет волшебства')
        assert books.favorites == ['Дюна', 'Хоббит, или туда и обратно']

    def test_get_list_of_favorites_books_returns_books(self, books):
        assert books.get_list_of_favorites_books() == ['Дюна', 'Хоббит, или туда и обратно']