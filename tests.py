from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert collector.books_genre == {'Гордость и предубеждение и зомби': '', 'Что делать, если ваш кот хочет вас убить': ''}


#2

    def test_set_book_genre_check_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        assert collector.books_genre == {'Гордость и предубеждение и зомби': 'Ужасы'}

#3
    @pytest.mark.parametrize('book,genre', [['Гордость и предубеждение и зомби', 'Ужасы'],['Что делать, если ваш кот хочет вас убить', 'Фантастика']])
    def test_get_book_genre_get_genre(self, book, genre):
        collector = BooksCollector()
        collector.books_genre = {book: genre}
        assert collector.get_book_genre(book) == genre

#4

    def test_get_books_with_specific_genre_fantasy_genre(self):
        collector = BooksCollector()
        collector.books_genre = {'Что делать, если ваш кот хочет вас убить': 'Фантастика'}
        assert collector.get_books_with_specific_genre('Фантастика') == ['Что делать, если ваш кот хочет вас убить']

#5

    def test_get_books_genre_get_books_dictionary(self):
        collector = BooksCollector()
        collector.books_genre = {'Гордость и предубеждение и зомби': 'Ужасы'}
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': 'Ужасы'}

#6

    def test_get_books_for_children_genre_for_children(self):
        collector = BooksCollector()
        collector.books_genre = {'Зверополис': 'Мультфильмы', 'Гордость и предубеждение и зомби': 'Ужасы'}
        assert collector.get_books_for_children() == ['Зверополис']

#7

    def test_dd_book_in_favorites_add_one_book(self):
        collector = BooksCollector()
        collector.books_genre = {'Зверополис': 'Мультфильмы'}
        collector.add_book_in_favorites('Зверополис')
        assert collector.favorites == ['Зверополис']

#8

    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()
        collector.favorites == ['Зверополис']
        collector.delete_book_from_favorites('Зверополис')
        assert collector.favorites == []

#9

    def test_get_list_of_favorites_books_get_list_wth_one_book(self):
        collector = BooksCollector()
        collector.favorites = ['Зверополис']
        assert collector.get_list_of_favorites_books() == ['Зверополис']