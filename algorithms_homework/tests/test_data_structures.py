import random
import unittest

from data_structures import AVLTree, Deque, DynamicArray, LinkedList


class TestLinearStructures(unittest.TestCase):
    def test_basic_operations(self):
        for klass in (DynamicArray, LinkedList, Deque):
            with self.subTest(structure=klass.__name__):
                structure = klass([10, 20, 30])
                self.assertEqual(len(structure), 3)
                self.assertEqual(structure.get(0), 10)
                self.assertEqual(structure.get(2), 30)
                self.assertEqual(structure.find(20), 1)
                self.assertEqual(structure.find(999), -1)
                structure.insert(1, 15)
                self.assertEqual(structure.to_list(), [10, 15, 20, 30])
                structure.insert(0, 5)
                structure.insert(len(structure), 40)
                self.assertEqual(structure.to_list(), [5, 10, 15, 20, 30, 40])
                self.assertEqual(structure.delete(2), 15)
                self.assertEqual(structure.delete(0), 5)
                self.assertEqual(structure.delete(len(structure) - 1), 40)
                self.assertEqual(structure.to_list(), [10, 20, 30])

    def test_empty_and_invalid_index(self):
        for klass in (DynamicArray, LinkedList, Deque):
            with self.subTest(structure=klass.__name__):
                structure = klass()
                self.assertEqual(structure.to_list(), [])
                self.assertEqual(structure.find(1), -1)
                with self.assertRaises(IndexError):
                    structure.get(0)
                with self.assertRaises(IndexError):
                    structure.delete(0)
                with self.assertRaises(IndexError):
                    structure.insert(-1, 99)
                with self.assertRaises(IndexError):
                    structure.insert(1, 99)
                structure.insert(0, None)
                self.assertEqual(structure.get(0), None)
                self.assertEqual(structure.delete(0), None)
                self.assertEqual(len(structure), 0)

    def test_array_grows(self):
        array = DynamicArray()
        for value in range(100):
            array.append(value)
        self.assertEqual(array.to_list(), list(range(100)))
        self.assertEqual(array.get(99), 99)

    def test_deque_ends(self):
        deq = Deque()
        with self.assertRaises(IndexError):
            deq.pop()
        with self.assertRaises(IndexError):
            deq.popleft()
        deq.appendleft(2)
        deq.appendleft(1)
        deq.append(3)
        deq.insert(2, 100)
        self.assertEqual(deq.to_list(), [1, 2, 100, 3])
        self.assertEqual(deq.delete(2), 100)
        self.assertEqual(deq.popleft(), 1)
        self.assertEqual(deq.pop(), 3)
        self.assertEqual(deq.pop(), 2)
        self.assertEqual(deq.to_list(), [])
        deq.appendleft(7)
        self.assertEqual(deq.pop(), 7)

    def test_randomized_against_python_list(self):
        rng = random.Random(42)
        for klass in (DynamicArray, LinkedList, Deque):
            with self.subTest(structure=klass.__name__):
                actual, expected = klass(), []
                for _ in range(300):
                    operation = rng.choice(["insert", "delete", "get"])
                    if operation == "insert" or not expected:
                        index = rng.randrange(len(expected) + 1)
                        value = rng.randrange(-100, 101)
                        actual.insert(index, value)
                        expected.insert(index, value)
                    elif operation == "delete":
                        index = rng.randrange(len(expected))
                        self.assertEqual(actual.delete(index), expected.pop(index))
                    else:
                        index = rng.randrange(len(expected))
                        self.assertEqual(actual.get(index), expected[index])
                    self.assertEqual(actual.to_list(), expected)
                    self.assertEqual(len(actual), len(expected))


class TestAVLTree(unittest.TestCase):
    def check_invariant(self, node):
        if node is None:
            return 0
        left_height = self.check_invariant(node.left)
        right_height = self.check_invariant(node.right)
        self.assertLessEqual(abs(left_height - right_height), 1)
        self.assertEqual(node.height, 1 + max(left_height, right_height))
        return node.height

    def test_all_rotation_cases(self):
        for numbers in ([30, 20, 10], [10, 20, 30], [30, 10, 20], [10, 30, 20]):
            with self.subTest(numbers=numbers):
                tree = AVLTree(numbers)
                self.assertEqual(tree.inorder(), [10, 20, 30])
                self.assertEqual(tree._root.key, 20)
                self.assertEqual(tree.height, 2)
                self.check_invariant(tree._root)

    def test_search_duplicates_delete(self):
        tree = AVLTree([50, 30, 70, 20, 40, 60, 80])
        self.assertTrue(tree.search(60))
        self.assertFalse(tree.search(999))
        self.assertFalse(tree.insert(40))
        self.assertEqual(len(tree), 7)
        self.assertTrue(tree.delete(50))  # Два потомка
        self.assertTrue(tree.delete(20))  # Лист
        self.assertFalse(tree.delete(999))
        self.assertEqual(tree.inorder(), [30, 40, 60, 70, 80])
        self.assertEqual(len(tree), 5)
        self.check_invariant(tree._root)

    def test_randomized(self):
        numbers = list(range(150))
        random.Random(123).shuffle(numbers)
        tree = AVLTree(numbers)
        self.assertEqual(tree.inorder(), list(range(150)))
        self.check_invariant(tree._root)
        random.Random(456).shuffle(numbers)
        for value in numbers:
            self.assertTrue(tree.delete(value))
            self.assertFalse(tree.search(value))
            self.check_invariant(tree._root)
        self.assertEqual(len(tree), 0)
        self.assertEqual(tree.height, 0)
        self.assertEqual(tree.inorder(), [])


if __name__ == "__main__":
    unittest.main()
