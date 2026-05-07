dataset = [68, 63, 22, 98, 84, 87, 13, 92, 32, 30]
pivot = dataset[0]
i = -1
j = len(dataset)

while True:
    i += 1
    while dataset[i] < pivot: 
        i += 1
    j -= 1
    while dataset[j] > pivot: 
        j -= 1
    if i >= j:
        break
    dataset[i], dataset[j] = dataset[j], dataset[i]
    print(dataset)
print(dataset)