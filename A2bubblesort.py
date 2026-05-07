data = [68, 63, 22, 98, 84, 87, 13, 92, 32, 30]
def bsort(arr):
    n = len(arr)
    for i in range(3):
        swapped = False
        print("Pass {i + 1}:")
        for j in range(0, n - 1 - i):
            print(f"Compare {arr[j]} and {arr[j + 1]}")
            if arr[j] > arr[j + 1]:
                print(f"Swap {arr[j]} and {arr[j + 1]}")
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        print(f"Array after pass {i + 1}:")
        print(arr)
        if not swapped:
            print("Early Exit")
            break

arr = data.copy()
bsort(arr)