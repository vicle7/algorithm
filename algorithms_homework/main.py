from data_structures import DynamicArray, LinkedList, Deque, AVLTree
from sorting import bubble_sort, quick_sort


def main():
    print("Массив")
    array = DynamicArray([10, 20, 30])
    array.insert(1, 15)
    print("После вставки:", array.to_list())
    print("По индексу 2:", array.get(2))
    print("Найти 30 (индекс):", array.find(30))
    print("Удалили:", array.delete(0), "; осталось:", array.to_list())

    print("\nСвязный список")
    linked = LinkedList([10, 20, 30])
    linked.insert(1, 15)
    print("После вставки:", linked.to_list())
    print("По индексу 2:", linked.get(2))
    print("Найти 30 (индекс):", linked.find(30))
    print("Удалили:", linked.delete(0), "; осталось:", linked.to_list())

    print("\nДек")
    deq = Deque([20, 30])
    deq.appendleft(10)
    deq.append(40)
    print("После вставок:", deq.to_list())
    print("Взять по индексу 1:", deq.get(1))
    print("Найти 30 (индекс):", deq.find(30))
    print("Удалили слева:", deq.popleft(), "; справа:", deq.pop())
    print("Осталось:", deq.to_list())

    print("\nAVL-дерево")
    tree = AVLTree([30, 20, 10, 40, 35])
    print("Отсортированные ключи:", tree.inorder())
    print("Поиск ключа 35:", tree.search(35))
    print("Удалили 20:", tree.delete(20))
    print("После удаления:", tree.inorder(), "; высота:", tree.height)

    print("\nСортировки")
    values = [5, 1, 4, 2, 8, 1]
    print("Исходный список:", values)
    print("Пузырёк:", bubble_sort(values))
    print("Быстрая:", quick_sort(values))


if __name__ == "__main__":
    main()
