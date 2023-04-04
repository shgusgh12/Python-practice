arr=  [3,1,2,5,7,8,6,11]


#정렬 가정 후
def merge(arr, p, q, r):
    n1 = p - q + 1
    n2 = r - q
    L = [0] * (n1 + 1)
    R = [0] * (n2 + 1)

    for i in range(n1):
        L[i] = arr[p+i]
    for i in range(n2):
        R[i] = arr[q+1+i]
    L[n1] = 10000000
    R[n2] = 10000000
    i = 0
    j = 0
    for k in range(p, r+1):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i = i+1
        else: 
            arr[k] = R[j]
            j = j+1


def MergeSort(arr, p, r):
    if p < r:
        q = (p + r) // 2
        MergeSort(arr,p, q)
        MergeSort(arr,q+1,r)
        merge(arr,p,q,r)


MergeSort(arr,0,7)
