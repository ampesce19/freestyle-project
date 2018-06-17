import pytest
from app.quiz import response_count

#if __name__ == "__main__":
#    response_count ()

def test_response_count_1():
    answers == "a"
    assert atotal == 1
    #expected to pass

def test_response_count_2():
    answers == "c"
    assert btotal == 1
    #expected to fail

def test_response_count_3():
    answers == "B"
    assert btotal ==1
    #expected to pass - checking capitalized letter

def test_response_count_4():
    answers == 1234
    assert atotal = btotal = ctotal = dtotal == 0
    #expected to pass
