from hello import add, multiply, subtract, divide


def test_add():
    assert 2 == add(1, 1)
    
    
def test_multiply():
    assert 10 == multiply(2, 5)
    
    
def test_subtract():
    assert 3 == subtract(9,6)
    

def test_divide():
    assert 10 == divide(100,10)
