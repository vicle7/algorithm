class DynamicArray:
    def __init__(self, values=()):
        self._capacity = 4
        self._data = [None] * self._capacity
        self._size = 0
        for value in values:
            self.append(value)

    def __len__(self):
        return self._size

    def _grow(self):
        self._capacity *= 2
        new_data = [None] * self._capacity
        for i in range(self._size):
            new_data[i] = self._data[i]
        self._data = new_data

    def get(self, index):
        if not 0 <= index < self._size:
            raise IndexError("Индекс вне массива")
        return self._data[index]

    def find(self, value):
        for i in range(self._size):
            if self._data[i] == value:
                return i
        return -1

    def insert(self, index, value):
        if not 0 <= index <= self._size:
            raise IndexError("Индекс вне массива")
        if self._size == self._capacity:
            self._grow()
        for i in range(self._size, index, -1):
            self._data[i] = self._data[i - 1]
        self._data[index] = value
        self._size += 1

    def append(self, value):
        self.insert(self._size, value)

    def delete(self, index):
        value = self.get(index)
        for i in range(index, self._size - 1):
            self._data[i] = self._data[i + 1]
        self._size -= 1
        self._data[self._size] = None
        return value

    def to_list(self):
        return [self._data[i] for i in range(self._size)]
