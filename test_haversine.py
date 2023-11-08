#test all five functions mysqrt, mycos, myarcsin, mysin and myhaversine individually :)
from myfunctions import mysqrt, myarcsin, mysin, mycos
from myhaversine import myhaversine


def test_mysqrt():
    assert mysqrt(0) == 0
    assert mysqrt(-1) == 0 
    assert mysqrt(9) == 3


def test_myarcsin():
    assert myarcsin(-2) == -90
    assert myarcsin(2) == 90
    assert myarcsin(0.5) == 30


def test_mysin():
    assert mysin(0) == 0
    assert mysin(90) == 1


def test_mycos():
    assert mycos(0) == 1
    assert mycos(90) == 0


def test_myhaversine(): 
    assert myhaversine((0, 0), (0, 0)) == 0
    assert myhaversine((90, 180), (90, 180)) == 0
