from typing import List

from domain.entities.book import Book
from use_cases.services.books_getter import BooksGetter


class GetBooksUseCase:
    def __init__(
        self,
        books_getter: BooksGetter
    ) -> None:
        self.__books_getter = books_getter

    def get(self, author_id: int) -> List[Book]:
        books = self.__books_getter.get(author_id)

        return books
