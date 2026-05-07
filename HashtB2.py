dataset = [68, 63, 22, 98, 84, 87, 13, 92, 32, 30]
m = 7
hash_table = [None] * m
count = 0
for key in dataset:
    if count == m: 
        break
    index = key % m
    while hash_table[index] is not None:
        index = (index + 1) % m
    hash_table[index] = key
    count += 1
print(hash_table)