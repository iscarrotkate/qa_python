# qa_python

## Unit tests
1. test_default_initialisation_values_true <br>
Проверяет значения атрибутов по умолчанию при инициализаии объекта
2. test_add_new_book_unique_valid_name_added <br>
Проверяет добавление книг с валидными названиями разной длинны
3. test_add_new_book_non_unique_name_original_list_not_changed <br>
Проверяет неизменность списка книга при попытке добавления уже добавленной книги
4. test_add_new_book_invalid_name_length_not_added <br>
Проверяет попытку добавления книг с названиями невалидной длинны
5. test_set_book_genre_valid_data_gener_is_set <br>
Проверяет присваивание жанра добавленным книгам: первое присвоение жарнра, присвоение того же значения, изменение жанра
6. test_set_book_genre_invalid_data_gener_is_not_set <br>
Проверяет попытку присвоения, когда жанр и/или книга не существуют 
7. test_get_book_genre_exiting_book_returns_genre <br>
Проверяет, что по названию существущей в списке книги возвращается релевантный жанр
8. test_get_books_with_specific_genre_valid_genre_return_books <br>
Проверяет, что по названию жанра возвращается релевантный список книг: нет книг жанра, есть одна книга, есть несколько книг
9. test_get_books_with_specific_genre_invalid_genre_return_empty_list <br>
Проверяет, что при попытке запроса несуществующего жанра возвращается пустой список
11. test_get_books_genre_return_several_items <br>
Проверяет, что метод возвращает релевантный набор книг
12. test_get_books_for_children_several_children_books_return_books <br>
Проверяет, что метод возвращает только те книги, которые принадлежат к жанрам, разрешенным детям
13. test_get_books_for_children_no_children_books_return_empty_list <br>
Проверят, что при отсутствии книг, разрешенных детям, возвращается путой список
14. test_add_book_in_favorites_existing_book_added <br>
Проверяет добавление существующих в списке книг в избранное
15. test_add_book_in_favorites_invalid_book_not_added <br>
Проверяет попытку добавления несуществующей в списке книги или уже добавленной книги
16. test_delete_book_from_favorites_exiting_book_removed <br>
Проверяет удаление книги из избранного 
17. test_delete_book_from_favorites_remove_non_exising_book_list_not_changed <br>
Проверяет попытку удаления несуществующей в избранном книги
18. test_get_list_of_favorites_books_returns_books <br>
Проверяет, что метод возвращает релевантный набор книг в избранном