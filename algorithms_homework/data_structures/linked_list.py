from dataclasses import dataclass


@dataclass
class _Node:
    value: object
    next: "_Node | None" = None


class LinkedList:
    def __init__(self, values=()):
        self._head = None
        self._size = 0
        for value in values:
            self.append(value)

    def __len__(self):
        return self._size

    def _node_at(self, index):
        if not 0 <= index < self._size:
            raise IndexError("Индекс вне списка")
        node = self._head
        for _ in range(index):
            node = node.next
        return node

    def get(self, index):
        return self._node_at(index).value

    def find(self, value):
        current = self._head
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def insert(self, index, value):
        if not 0 <= index <= self._size:
            raise IndexError("Индекс вне списка")
        if index == 0:
            self._head = _Node(value, self._head)
        else:
            previous = self._node_at(index - 1)
            previous.next = _Node(value, previous.next)
        self._size += 1

    def append(self, value):
        self.insert(self._size, value)

    def delete(self, index):
        if not 0 <= index < self._size:
            raise IndexError("Индекс вне списка")
        if index == 0:
            value = self._head.value
            self._head = self._head.next
        else:
            previous = self._node_at(index - 1)
            value = previous.next.value
            previous.next = previous.next.next
        self._size -= 1
        return value

    def to_list(self):
        result = []
        current = self._head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result
