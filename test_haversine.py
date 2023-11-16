#test all five functions mysqrt, mycos, myarcsin, mysin and myhaversine individually :)
from myfunctions import mysqrt, myarcsin, mysin, mycos
from myhaversine import myhaversine

def test_mysqrt():
    tol = 10**-5
    assert -tol < mysqrt(0) < tol
    assert mysqrt(-1) == 0 
    assert 3-tol < mysqrt(9) < 3+tol



def test_myarcsin():
    tol = 10**-5
    assert myarcsin(-2) == -90
    assert myarcsin(2) == 90
    assert 30 - tol < myarcsin(0.5) < 30 + tol



def test_mysin():
    tol = 10**-5
    assert -tol < mysin(0) < tol
    assert 1-tol < mysin(90) < 1+tol

def test_mycos():
    tol = 10**-5
    assert 1-tol < mycos(0) < 1+tol
    assert -tol < mycos(90) < tol


def test_myhaversine(): 
    tol = 10**-1
    assert -tol<myhaversine((0, 0), (0, 0))<tol
    assert -tol<myhaversine((90, 180), (90, 180))<tol
 