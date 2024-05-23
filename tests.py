import pytest


class TestBooksCollector:
    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2
        assert 'Гордость и предубеждение и зомби' in collector.get_books_genre()
        assert 'Что делать, если ваш кот хочет вас убить' in collector.get_books_genre()

    @pytest.mark.parametrize('new_book', ['A', 'А' * 40])
    def test_add_new_book_with_name_between_1_and_40_characters(self, collector, new_book):
        collector.add_new_book(new_book)
        assert collector.get_book_genre(new_book) is not None

    @pytest.mark.parametrize('new_book', ['', 'А' * 41])
    def test_add_new_book_with_name_0_and_41_characters(self, collector, new_book):
        collector.add_new_book(new_book)
        assert collector.get_book_genre(new_book) is None

    def test_add_new_book_add_the_same_book_twice(self, collector_with_the_book, the_book):
        collector_with_the_book.add_new_book(the_book)
        assert len(collector_with_the_book.get_books_genre()) == 1

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_set_book_correct_genre(self, collector_with_the_book, the_book, genre):
        collector_with_the_book.set_book_genre(the_book, genre)
        assert collector_with_the_book.get_book_genre(the_book) == genre

    def test_set_book_genre_set_book_incorrect_genre(self, collector_with_the_book, the_book):
        collector_with_the_book.set_book_genre(the_book, 'Комикс')
        assert collector_with_the_book.get_book_genre(the_book) == ''

    def test_get_book_genre_get_genre_for_incorrect_book(self, collector_with_the_book, the_book):
        assert collector_with_the_book.get_book_genre(the_book + '2') is None

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_books_with_specific_genre_get_genre_for_two_books(self, collector, genre):
        new_book_1 = 'Братья'
        new_book_2 = 'Сестры'
        collector.add_new_book(new_book_1)
        collector.set_book_genre(new_book_1, genre)
        collector.add_new_book(new_book_2)
        collector.set_book_genre(new_book_2, genre)
        books = collector.get_books_with_specific_genre(genre)
        assert len(books) == 2
        assert new_book_1 in books
        assert new_book_2 in books

    def test_add_book_in_favorites_add_in_favorites_one_book(self, collector_with_the_book, the_book):
        assert len(collector_with_the_book.get_list_of_favorites_books()) == 0
        collector_with_the_book.add_book_in_favorites(the_book)
        assert collector_with_the_book.get_list_of_favorites_books() == [the_book]

    def test_delete_book_from_favorites_delete_1_book_from_favorites(self, collector_with_the_book, the_book):
        collector_with_the_book.add_book_in_favorites(the_book)
        collector_with_the_book.delete_book_from_favorites(the_book)
        assert len(collector_with_the_book.get_books_genre()) == 1
        assert len(collector_with_the_book.get_list_of_favorites_books()) == 0

    def test_get_books_for_children_get_3_books_for_children(self, collector):
        books = ['Незнайка', 'Эмили и Марго', 'Жуль Верн', 'Вафельное сердце', 'Золушка']
        genres = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        for book, genre in zip(books, genres):
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)
        books_for_children = collector.get_books_for_children()
        assert len(books_for_children) == 3
        assert 'Незнайка' in books_for_children
        assert 'Вафельное сердце' in books_for_children
        assert 'Золушка' in books_for_children

    def test_get_books_genre_get_books_genre_of_1_book(self, collector_with_the_book, the_book):
        assert len(collector_with_the_book.get_books_genre()) == 1
        assert the_book in collector_with_the_book.get_books_genre()

    def test_get_list_of_favorites_books_get_2_favorites_books(self, collector_with_the_book, the_book):
        collector_with_the_book.add_new_book(the_book + '2')
        collector_with_the_book.add_book_in_favorites(the_book)
        collector_with_the_book.add_book_in_favorites(the_book + '2')
        assert len(collector_with_the_book.get_list_of_favorites_books()) == 2
        assert the_book in collector_with_the_book.get_list_of_favorites_books()
        assert the_book + '2' in collector_with_the_book.get_list_of_favorites_books()
