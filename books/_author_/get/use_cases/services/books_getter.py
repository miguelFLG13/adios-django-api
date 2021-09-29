from typing import List

from domain.entities.book import Book
from domain.repositories.book_repository.book_repository import BookRepository


class BooksGetter:
    def __init__(self, book_repository: BookRepository) -> None:
        self.__book_repository = book_repository

    def get(self, author_id: int) -> List[Book]:
        books = self.__asset_repository.find_by_author(author_id)
        
        return books
