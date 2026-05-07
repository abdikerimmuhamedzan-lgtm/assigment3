dataset = [68, 63, 22, 98, 84, 87, 13, 92, 32, 30]

def get_min_max(arr, low, high):
    if low == high: 
        return arr[low], arr[low]
    if high == low + 1:
        return (arr[low], arr[high]) if arr[low] < arr[high] else (arr[high], arr[low])
    
    mid = (low + high) // 2
    left_min, left_max = get_min_max(arr, low, mid)
    right_min, right_max = get_min_max(arr, mid + 1, high)
    
    final_min = left_min if left_min < right_min else right_min
    final_max = left_max if left_max > right_max else right_max
    return final_min, final_max

min_val, max_val = get_min_max(dataset, 0, len(dataset) - 1)
print(max_val - min_val)