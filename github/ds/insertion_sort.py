arr = [5,2,1,8,3,7,10]

for i in range(1,len(arr)):
    key = arr[i]
    j = i-1
    while j > -1 and key < arr[j]:
        arr[j+1] = arr[j]
        j = j - 1
    arr[j + 1] = key

print(arr)


