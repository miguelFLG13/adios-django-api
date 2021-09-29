from unittest import TestCase
from dataclass_bakery import baker

from domain.entities.book import Book
from use_cases.services.book_creator import BookCreator


class TestBookCreator(TestCase):

    def test_create_book_ok(self):
        """
        
        """
        book_repository = 
        book_creator = BookCreator(book_repository)
        book = baker.make(Book)
        new_book = book_creator.create(book)

        self.assertTrue(is_instance(new_book, Book))
        self.assertEqual(new_book.isbn, book.isbn)
