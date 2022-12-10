import pytest
from src.util import same_strings

def test_same_strings():
    assert same_strings('ben','Ben') == True

def test_not_same_strings():
    assert same_strings('ben','Bein') == False