import pytest
from jar import Jar

def test_init():
    # Test that jar initializes with the right capacity and size
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0

    # Test default capacity is 12
    default_jar = Jar()
    assert default_jar.capacity == 12

    # Test that invalid capacities raise ValueError
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar(12.5)

def test_str():
    # Test the __str__ method returns the correct number of cookies
    jar = Jar(5)
    # Initially, the jar is empty
    assert str(jar) == ""

    jar.deposit(3)
    # Now, __str__ should return three cookie emojis
    assert str(jar) == "🍪" * 3

def test_deposit():
    jar = Jar(5)
    jar.deposit(3)
    assert jar.size == 3

    # Depositing more cookies up to the capacity should work
    jar.deposit(2)
    assert jar.size == 5

    # Depositing beyond capacity should raise ValueError
    with pytest.raises(ValueError):
        jar.deposit(1)

    # Depositing a negative number should also raise ValueError
    with pytest.raises(ValueError):
        jar.deposit(-1)

def test_withdraw():
    jar = Jar(5)
    jar.deposit(5)
    jar.withdraw(3)
    assert jar.size == 2

    # Withdrawing more cookies than are in the jar should raise ValueError
    with pytest.raises(ValueError):
        jar.withdraw(3)

    # Withdrawing a negative number should also raise ValueError
    with pytest.raises(ValueError):
        jar.withdraw(-1)
