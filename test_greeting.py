
import pytest
from greeting import greet


def test_greet():
    assert greet("Ali") == "Hello, Ali!"


def test_greet_another_name():
    assert greet("Sara") == "Hello, Sara!"


def test_empty_name():
    with pytest.raises(ValueError):
        greet("")


def test_spaces_only():
    with pytest.raises(ValueError):
        greet("   ")
