arr = [-1000000, 16, 14, 10, 8, 7,9,3,2,4,1]
heap = len(arr) - 1
def MaxHeapify(arr, i):
    l = 2*i 
    r = 2*i + 1
    largest = 0
    if l <= heap and arr[l] > arr[i]:
        largest = l
    else:
        largest = i
    if r <= heap and arr[r] > arr[largest]:  #왼쪽 자식노드와 오른쪽 자식 노드 비교
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        MaxHeapify(arr, largest)


def BuildMaxHeap(arr):
    for i in range((len(arr)-1)//2, 0, -1):
        MaxHeapify(arr,i)
    


def HeapSort(arr):
    BuildMaxHeap(arr)
    for i in range(len(arr)-1,0,-1):
        arr[1], arr[i] = arr[i], arr[1]
        global heap 
        heap = heap - 1
        MaxHeapify(arr,1)

HeapSort(arr)

print(arr)

