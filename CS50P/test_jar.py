from jar import Jar
import pytest


def test_properties():
    jar = Jar()
    # Changing instance's state and asserting its value
    jar.size = 3
    assert jar.size == 3
    # Asserting not an int error
    with pytest.raises(ValueError):
        jar.size = 3.3
    jar.capacity = 9
    assert jar.capacity == 9
    with pytest.raises(ValueError):
        jar.capacity = 9.9

def test_deposit():
    jar = Jar()
    # Calling function
    jar.deposit(3)
    # Asserting change in instance's state
    assert jar.size == 3
    # Asserting negative value error
    with pytest.raises(ValueError):
        jar.deposit(-3)
    # Asserting jar overflow error
    with pytest.raises(ValueError):
        jar.deposit(13)

def test_withdraw():
    jar = Jar()
    # Changing state
    jar.size = 6
    # Calling function
    jar.withdraw(4)
    # Asserting change in instance's state
    assert jar.size == 2
    # Emptying jar
    jar.withdraw(2)
    # Asserting empty jar
    assert jar.size == 0
    # Asserting negative value error
    with pytest.raises(ValueError):
        jar.withdraw(-3)
    # Asserting emtpied jar error
    with pytest.raises(ValueError):
        jar.withdraw(13)


def test_str():
    jar = Jar()
    # Changing state with correct function
    jar.deposit(6)
    # Asserting str
    assert str(jar) == "🍪🍪🍪🍪🍪🍪"
    # Changing state again to empty the jar
    jar.withdraw(6)
    # Asserting str
    assert str(jar) == ""