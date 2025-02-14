class BooksCollector:
    def __init__(self):
        self.books_genre = {}
        self.favorites = []
        self.genres = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        self.genre_age_rating = ['Ужасы', 'Детективы']

    def add_new_book(self, title):
        if title not in self.books_genre and 0 < len(title) < 41:
            self.books_genre[title] = ''

    def set_book_genre(self, title, genre):
        if title in self.books_genre and genre in self.genres:
            self.books_genre[title] = genre

    def get_book_genre(self, title):
        return self.books_genre.get(title)

    def get_books_with_specific_genre(self, genre):
        books_with_specific_genre = []
        if self.books_genre and genre in self.genres:
            for book_title, book_genre in self.books_genre.items():
                if book_genre == genre:
                    books_with_specific_genre.append(book_title)
        return books_with_specific_genre

    def get_books_genre(self):
        return self.books_genre.copy()

    def get_books_for_children(self):
        books_for_children = []
        for title, genre in self.books_genre.items():
            if genre not in self.genre_age_rating:
                books_for_children.append(title)
        return books_for_children

    def add_book_to_favorites(self, title):
        if title in self.books_genre and title not in self.favorites:
            self.favorites.append(title)

    def remove_book_from_favorites(self, title):
        if title in self.favorites:
            self.favorites.remove(title)

    def get_list_of_favorite_books(self):
        return self.favorites.copy()