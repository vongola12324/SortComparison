def sort(data):
    for i in range((len(data) - 2) // 2, -1, -1):
        heapify(data, i, len(data) - 1)

    for i in range(len(data) - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, 0, i - 1)


def heapify(data, start, end):
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        if child + 1 <= end and data[child] < data[child + 1]:
            child += 1
        if data[root] < data[child]:
            data[root], data[child] = data[child], data[root]
            root = child
        else:
            break
