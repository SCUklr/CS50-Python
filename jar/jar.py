class Jar:
    def __init__(self, capacity=12):
        # Ensure capacity is a non-negative integer
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative int")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        # Return a string with one cookie ("🍪") for each cookie in the jar
        return "🍪" * self._size

    def deposit(self, n):
        # Optionally, you may also reject negative numbers (so that deposit is not abused)
        if n < 0:
            raise ValueError("Cannot deposit a negative number of cookies")
        if self._size + n > self._capacity:
            raise ValueError("Deposit would exceed jar capacity")
        self._size += n

    def withdraw(self, n):
        if n < 0:
            raise ValueError("Cannot withdraw a negative number of cookies")
        if n > self._size:
            raise ValueError("Not enough cookies in the jar")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
