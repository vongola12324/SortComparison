def sort(data):
    if len(data) < 1:
        return

    for i in range(len(data)):
        index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[index]:
                index = j
        if index != i:
            data[index], data[i] = data[i], data[index]
