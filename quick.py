def sort(data):
    if len(data) <= 1:
        return
    _sort(data, 0, len(data)-1)


def _sort(data, left, right):
    if left < right:
        pivot = partition(data, left, right)
        _sort(data, left, pivot - 1)
        _sort(data, pivot + 1, right)


def partition(data, left, right):
    pivot = (left + right) // 2
    data[pivot], data[right] = data[right], data[pivot]
    for i in range(left, right):
        if data[i] <= data[right]:
            data[i], data[left] = data[left], data[i]
            left += 1

    data[left], data[right] = data[right], data[left]
    return left
