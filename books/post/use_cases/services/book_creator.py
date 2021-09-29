from typing import List

from domain.entities.book import Book
from domain.repositories.book_repository.book_repository import BookRepository


class BookCreator:
    def __init__(self, book_repository: BookRepository) -> None:
        self.__book_repository = book_repository

    def create(self, book: Book) -> Book:
        book = self.__asset_repository.create(book)
        
        return book
