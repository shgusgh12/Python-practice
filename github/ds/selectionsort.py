n = int(input())
array = []
for i in range(n):
    array.append(int(input()))

for i in range(len(array)):
    min_idx = i
    for j in range(i+1, len(array)):
        if array[min_idx] > array[j]:
            min_idx = j
    array[min_idx], array[i] = array[i] , array[min_idx]

print(array)
            
