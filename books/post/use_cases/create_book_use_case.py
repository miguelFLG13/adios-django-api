from typing import List

from domain.entities.book import Book
from use_cases.services.book_creator import BookCreator


class CreateBookUseCase:
    def __init__(
        self,
        book_creator: BookCreator
    ) -> None:
        self.__book_creator = books_creator

    def create(self, book: Book) -> Book:
        book = self.__book_creator.create(book)

        return book
