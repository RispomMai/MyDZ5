import math

def test_filter_python():
    assert list(filter(lambda x : x > 3 ,[1, 2, 3, 4, 5])) == [4, 5]

def test_map_python():
    assert list(map(lambda x: x ** 2,[1, 2, 3, 4, 5])) == [1,4,9,16,25]

def test_sorted_python():
    assert list(sorted([2, 5, 3, 1, 4])) == [1,2,3,4,5]
    assert list(sorted([2, 5, 3, 1, 4],reverse=True)) == [5, 4, 3, 2, 1]

def test_pi_math_python():
    assert math.pi == 3.141592653589793
    assert math.cos(math.pi) == -1
    assert round(math.sin(math.pi),1) == 0
def test_pow_math_python():
    assert math.pow(2,5) == 32
    assert round(math.pow(2.236, 2),3) == 5.0

def test_hypot_math_python():
    assert math.hypot(3, 4) == 5