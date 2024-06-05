import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hii", "Test failed due to strings do not match"

def test_secondCreditCardProgram():
    a = 4
    b = 6
    assert a+2 == b, "addition do not match"


