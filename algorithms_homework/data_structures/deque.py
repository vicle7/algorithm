from dataclasses import dataclass


@dataclass
class _Node:
    value: object
    prev: "_Node | None" = None
    next: "_Node | None" = None


class Deque:
    def __init__(self, values=()):
        self._head = None
        self._tail = None
        self._size = 0
        for value in values:
            self.append(value)

    def __len__(self):
        return self._size

    def append(self, value):
        node = _Node(value, prev=self._tail)
        if self._tail is None:
            self._head = node
        else:
            self._tail.next = node
        self._tail = node
        self._size += 1

    def appendleft(self, value):
        node = _Node(value, next=self._head)
        if self._head is None:
            self._tail = node
        else:
            self._head.prev = node
        self._head = node
        self._size += 1

    def _remove_node(self, node):
        if node.prev is None:
            self._head = node.next
        else:
            node.prev.next = node.next
        if node.next is None:
            self._tail = node.prev
        else:
            node.next.prev = node.prev
        self._size -= 1
        return node.value

    def pop(self):
        #Удаление справа: O(1)
        if self._tail is None:
            raise IndexError("Дек пуст")
        return self._remove_node(self._tail)

    def popleft(self):
        #Удаление слева: O(1)
        if self._head is None:
            raise IndexError("Дек пуст")
        return self._remove_node(self._head)

    def _node_at(self, index):
        if not 0 <= index < self._size:
            raise IndexError("Индекс вне дека")
        if index < self._size // 2:
            node = self._head
            for _ in range(index):
                node = node.next
        else:
            node = self._tail
            for _ in range(self._size - index - 1):
                node = node.prev
        return node

    def get(self, index):
        return self._node_at(index).value

    def find(self, value):
        node = self._head
        index = 0
        while node is not None:
            if node.value == value:
                return index
            node = node.next
            index += 1
        return -1

    def insert(self, index, value):
        #Вставка в любую позицию (в середину O(n))
        if not 0 <= index <= self._size:
            raise IndexError("Индекс вне дека")
        if index == 0:
            self.appendleft(value)
        elif index == self._size:
            self.append(value)
        else:
            next_node = self._node_at(index)
            node = _Node(value, prev=next_node.prev, next=next_node)
            next_node.prev.next = node
            next_node.prev = node
            self._size += 1

    def delete(self, index):
        return self._remove_node(self._node_at(index))

    def to_list(self):
        result = []
        node = self._head
        while node is not None:
            result.append(node.value)
            node = node.next
        return result
