import pytest

class TestBooksCollector:
    @pytest.fixture
    def collector(self):
        return BooksCollector() # type: ignore

    def test_add_new_book_success(self, collector):
        collector.add_new_book("Война и мир")
        assert "Война и мир" in collector.books_genre

    def test_add_new_book_already_exists(self, collector):
        collector.add_new_book("Война и мир")
        collector.add_new_book("Война и мир")
        assert list(collector.books_genre.keys()).count("Война и мир") == 1

    @pytest.mark.parametrize('name', ['a' * 41, ''])
    def test_add_new_book_invalid_name(self, collector, name):
        collector.add_new_book(name)
        assert len(collector.books_genre) == 0

    def test_set_book_genre_success(self, collector):
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Фантастика")
        assert collector.get_book_genre("Война и мир") == "Фантастика"

    def test_set_book_genre_book_not_exists(self, collector):
        collector.set_book_genre("Неизвестная книга", "Фантастика")
        assert collector.get_book_genre("Неизвестная книга") is None

    def test_add_book_to_favorites_success(self, collector):
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Фантастика")
        collector.add_book_to_favorites("Война и мир")
        assert "Война и мир" in collector.get_list_of_favorite_books()

    def test_remove_book_from_favorites_success(self, collector):
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Фантастика")
        collector.add_book_to_favorites("Война и мир")
        collector.remove_book_from_favorites("Война и мир")
        assert "Война и мир" not in collector.get_list_of_favorite_books()

    def test_get_books_for_children(self, collector):
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Мультфильмы")
        assert collector.get_books_for_children() == ["Война и мир"]

    # Более подробные тесты на зрительскую книгу вообще
    def test_get_list_of_favorite_books_empty(self, collector):
        assert collector.get_list_of_favorite_books() == []

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Фантастика")
        collector.add_new_book("Метро 2033")
        collector.set_book_genre("Метро 2033", "Фантастика")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Война и мир", "Метро 2033"]
    
    def test_get_books_with_specific_genre_not_exists(self, collector):
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Фантастика")
        assert collector.get_books_with_specific_genre("Ужасы") == []

    def test_get_books_genre_returns_dict(self, collector):
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Фантастика")
        assert isinstance(collector.get_books_genre(), dict)
    
    def test_get_books_genre_returns_copy(self, collector):
        collector.add_new_book("Война и мир")
        collector.set_book_genre("Война и мир", "Фантастика")
        books_genre_before = collector.get_books_genre()
        books_genre_before['Неизвестная книга'] = 'Жанр'
        assert collector.get_books_genre()['Война и мир'] == 'Фантастика'