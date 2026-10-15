def bubble_sort(values):
    items = list(values)
    for end in range(len(items) - 1, 0, -1):
        swapped = False
        for i in range(end):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                swapped = True
        if not swapped:
            break
    return items


def quick_sort(values):
    items = list(values)

    def partition(left, right):
        pivot = items[right]
        boundary = left
        for i in range(left, right):
            if items[i] <= pivot:
                items[i], items[boundary] = items[boundary], items[i]
                boundary += 1
        items[boundary], items[right] = items[right], items[boundary]
        return boundary

    def sort(left, right):
        if left >= right:
            return
        pivot_index = partition(left, right)
        sort(left, pivot_index - 1)
        sort(pivot_index + 1, right)

    sort(0, len(items) - 1)
    return items
