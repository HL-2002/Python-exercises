class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    def deposit(self, n):
        if n >= 0:
            if n + self.size <= self.capacity:
                self.size += n
            else:
                raise ValueError("Error: Jar overflow")
        else:
            raise ValueError("Error: Negative cookie amount")

    def withdraw(self, n):
        if n >= 0:
            if n <= self.size:
                self.size -= n
            else:
                raise ValueError("Error: Emptied jar")
        else:
            raise ValueError("Error: Negative cookie amount")


    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, n):
        if isinstance(n,int):
            self._capacity = n
        else:
            raise ValueError("Error: Not an integer")
    
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, n):
        if isinstance(n,int):
            self._size = n
        else:
            raise ValueError("Error: Not an integer")

    


def main():
    jar = Jar()
    jar.deposit(9)
    jar.withdraw(3)
    print(jar)


if __name__ == "__main__":
    main()