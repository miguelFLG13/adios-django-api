from unittest import TestCase
from dataclass_bakery import baker

from domain.entities.book import Book
from use_cases.services.book_creator import BookCreator


class TestBookCreator(TestCase):

    def test_create_book_ok(self):
        """
        Test book creation
        """
        book = baker.make(Book)
        book_repository = Mock()
        book_repository.create_book.return_value = book
        book_creator = BookCreator(book_repository)
        new_book = book_creator.create(book)

        self.assertTrue(is_instance(new_book, Book))
        self.assertEqual(new_book.isbn, book.isbn)
