dataset = [68, 63, 22, 98, 84, 87, 13, 92, 32, 30]
sort = sorted(dataset)
target = 13
low = 0
high = len(sort) - 1 
while low <= high:
    mid = (low + high) // 2
    print(low, high, mid)
    if sort[mid] == target:
        break
    elif sort[mid] > target:
        high = mid - 1
    else:
        low = mid + 1