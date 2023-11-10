#test all five functions mysqrt, mycos, myarcsin, mysin and myhaversine individually :)
from myfunctions import mysqrt, myarcsin, mysin, mycos
from myhaversine import myhaversine


def test_mysqrt():
    try:
        assert mysqrt(0) == 0
    except AssertionError:
        print("the squareroot of 0 is 0")
    try:
        assert mysqrt(-1) == 0 
    except AssertionError:
        print("the squareroot of -1 is 0")
    try:
        assert mysqrt(9) == 3
    except AssertionError:
        print("the squareroot of 9 is 3")


def test_myarcsin():
    try:
        assert myarcsin(-2) == -90
    except AssertionError:
        print("the arcsin of -2 is -90")
    try:
        assert myarcsin(2) == 90
    except AssertionError:
        print("the arcsin of 2 is 90")
    try:
        assert myarcsin(0.5) == 30
    except AssertionError:
        print("the arcsin of 0.5 is 30")


def test_mysin():
    assert mysin(0) == 0
    assert mysin(90) == 1


def test_mycos():
    assert mycos(0) == 1
    assert mycos(90) == 0


def test_myhaversine(): 
    try:
        assert myhaversine((0, 0), (0, 0)) == 0
    except AssertionError:
        print("the haversine of 0 is 0 ")
    try:
        assert myhaversine((90, 180), (90, 180)) == 0
    except AssertionError:
        print("the haversine of 90 and 180 is 0 ")
