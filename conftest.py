import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()

@pytest.fixture
def the_book():
    return 'Война и мир'

@pytest.fixture
def collector_with_the_book(the_book):
    collector = BooksCollector()
    collector.add_new_book(the_book)
    return collector
