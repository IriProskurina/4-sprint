import pytest

@pytest.fixture
def collector():
    return BooksCollector() # type: ignore

def test_add_new_book_success(collector):
    collector.add_new_book('Война и мир')
    assert 'Война и мир' in collector.books_genre

def test_add_new_book_already_exists(collector):
    collector.add_new_book('Война и мир')
    collector.add_new_book('Война и мир')  # попытаемся добавить снова
    assert len(collector.books_genre) == 1

def test_set_book_genre_success(collector):
    collector.add_new_book('Война и мир')
    collector.set_book_genre('Война и мир', 'Фантастика')
    assert 'Фантастика' in collector.books_genre['Война и мир']

def test_add_book_in_favorites_success(collector):
    collector.add_new_book('Война и мир')
    collector.set_book_genre('Война и мир', 'Фантастика')
    collector.add_book_in_favorites('Война и мир')
    assert 'Война и мир' in collector.get_list_of_favorites_books()

def test_delete_book_from_favorites_success(collector):
    collector.add_new_book('Война и мир')
    collector.set_book_genre('Война и мир', 'Фантастика')
    collector.add_book_in_favorites('Война и мир')
    collector.delete_book_from_favorites('Война и мир')
    assert 'Война и мир' not in collector.get_list_of_favorites_books()

def test_get_books_with_specific_genre_success(collector):
    collector.add_new_book('Война и мир')
    collector.set_book_genre('Война и мир', 'Фантастика')
    collector.add_new_book('Метро 2033')
    collector.set_book_genre('Метро 2033', 'Фантастика')
    assert collector.get_books_with_specific_genre('Фантастика') == ['Война и мир', 'Метро 2033']

def test_get_books_for_children_success(collector):
    collector.add_new_book('Война и мир')
    collector.set_book_genre('Война и мир', 'Мультфильмы')
    assert collector.get_books_for_children() == ['Война и мир']

def test_get_books_for_children_mixed_genres(collector):
    collector.add_new_book('Война и мир')
    collector.set_book_genre('Война и мир', 'Мультфильмы')
    collector.add_new_book('Оно')
    collector.set_book_genre('Оно', 'Ужасы')
    assert collector.get_books_for_children() == ['Война и мир']