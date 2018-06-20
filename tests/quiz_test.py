import pytest
from app.quiz import response_count

test_1 = response_count()

def test_response_count_1():
    test_1 == "a"
    assert atotal == 1
    #expected to pass

test_2 = response_count()

def test_response_count_2():
    test_2 == "c"
    assert btotal == 1
    #expected to fail

test_3 = response_count()

def test_response_count_3():
    test_3 == "B"
    assert btotal ==1
    #expected to pass - checking capitalized letter

test_4 = response_count()

def test_response_count_4():
    test_4 == 1234
    assert atotal == btotal == ctotal == dtotal == 0
    #expected to pass
