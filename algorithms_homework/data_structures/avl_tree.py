from dataclasses import dataclass


@dataclass
class _Node:
    key: int
    height: int = 1
    left: "_Node | None" = None
    right: "_Node | None" = None


class AVLTree:
    def __init__(self, values=()):
        self._root = None
        self._size = 0
        for key in values:
            self.insert(key)

    def __len__(self):
        return self._size

    @staticmethod
    def _height(node):
        return node.height if node else 0

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance_factor(self, node):
        return self._height(node.left) - self._height(node.right)

    def _rotate_right(self, top):
        new_top = top.left
        top.left = new_top.right
        new_top.right = top
        self._update_height(top)
        self._update_height(new_top)
        return new_top

    def _rotate_left(self, top):
        new_top = top.right
        top.right = new_top.left
        new_top.left = top
        self._update_height(top)
        self._update_height(new_top)
        return new_top

    def _rebalance(self, node):
        self._update_height(node)
        balance = self._balance_factor(node)
        if balance > 1:
            if self._balance_factor(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1:
            if self._balance_factor(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def search(self, key):
        #Поиск значения по ключу: O(log n)
        node = self._root
        while node is not None:
            if key == node.key:
                return True
            node = node.left if key < node.key else node.right
        return False

    def insert(self, key):
        #Вставка ключа: O(log n). Повторяющиеся ключи игнорируются
        if self.search(key):
            return False
        self._root = self._insert(self._root, key)
        self._size += 1
        return True

    def _insert(self, node, key):
        if node is None:
            return _Node(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return self._rebalance(node)

    def delete(self, key):
        #Удаление по ключу: O(log n)
        if not self.search(key):
            return False
        self._root = self._delete(self._root, key)
        self._size -= 1
        return True

    def _delete(self, node, key):
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            successor = node.right
            while successor.left is not None:
                successor = successor.left
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)
        return self._rebalance(node)

    @property
    def height(self):
        return self._height(self._root)

    def inorder(self):
        #Список ключей по возрастанию: O(n)
        result = []

        def walk(node):
            if node is None:
                return
            walk(node.left)
            result.append(node.key)
            walk(node.right)

        walk(self._root)
        return result
