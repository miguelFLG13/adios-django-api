from unittest import TestCase
from dataclass_bakery import baker

from domain.entities.book import Book
from use_cases.services.book_creator import BookCreator


class TestCreateBookUseCase(TestCase):

    def test_create_book_ok(self):
        """
        
        """
        book_creator = BookCreator()
        book = baker.make(Book)
        book_creator.create(book)
