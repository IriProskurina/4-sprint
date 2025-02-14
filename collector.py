class BooksCollector:
    def __init__(self):
        self.books_genre = {}
        self.favorites = []
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        self.genre_age_rating = ['Ужасы', 'Детективы']

    def add_new_book(self, name):
        if name not in self.books_genre and 0 < len(name) < 41:
            self.books_genre[name] = ''

    def set_book_genre(self, name, genre):
        if name in self.books_genre and genre in self.genre:
            self.books_genre[name] = genre

    def get_book_genre(self, name):
        return self.books_genre.get(name)

    def get_books_with_specific_genre(self, genre):
        return [name for name, book_genre in self.books_genre.items() if book_genre == genre]

    def add_book_to_favorites(self, name):
        if name in self.books_genre and name not in self.favorites:
            self.favorites.append(name)

    def remove_book_from_favorites(self, name):
        if name in self.favorites:
            self.favorites.remove(name)

    def get_list_of_favorite_books(self):
        return self.favorites.copy()  # Возвращаем копию списка

    def get_books_for_children(self):
        return [name for name, genre in self.books_genre.items() if genre not in self.genre_age_rating]

    def get_books_genre(self):
        return self.books_genre.copy()  # Возвращаем копию словаря
