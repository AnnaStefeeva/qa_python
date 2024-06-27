import pytest
from data import the_book
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


@pytest.fixture
def collector_with_the_book():
    collector = BooksCollector()
    collector.add_new_book(the_book)
    return collector
