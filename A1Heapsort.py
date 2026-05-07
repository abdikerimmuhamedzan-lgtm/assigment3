dataset = [68, 63, 22, 98, 84, 87, 13, 92, 32, 30]

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2   
    if l < n and arr[l] > arr[largest]: 
        largest = l        
    if r < n and arr[r] > arr[largest]: 
        largest = r        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
n = len(dataset)
for i in range(n // 2 - 1, -1, -1):
    heapify(dataset, n, i)
for i in range(n - 1, 0, -1):
    dataset[0], dataset[i] = dataset[i], dataset[0] 
    heapify(dataset, i, 0) 
print(dataset)