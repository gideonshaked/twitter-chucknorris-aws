import pytest
import main


def test_Joke1():
    assert isinstance(main.getJoke1(), str)


def test_Joke2():
    assert isinstance(main.getJoke2(), str)
