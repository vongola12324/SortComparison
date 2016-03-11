def sort(data):
    for i in range(len(data)):
        for j in range(i):
            if data[i] < data[j]:
                data[i], data[j] = data[j], data[i]
