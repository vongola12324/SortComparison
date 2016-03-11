def sort(data):
    if len(data) <= 1:
        return

    for i in range(1, len(data)):
        temp = data[i]
        j = i - 1
        while j >= 0 and temp < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = temp