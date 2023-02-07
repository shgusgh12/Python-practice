

arr = [2,5,4,6,10,1,3]
#insertion sort
def insertion_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
    print(arr)

#quick sort

def qsort(arr, start, end):
    #start end 각각 시작과 끝의 index
    if start >= end:
        return
    pivot = start #제일 처음값을 pivot으로 둔다
    left = start + 1
    right = end
    while left <= right:
        #left값을 더해 가면서 pivot보다 큰 값의 index 찾기
        while left <= end and arr[left] <= arr[pivot]:
            left+=1
        #right값을 빼가면서 pivot보다 작은 값의 index 찾기
        while right > start and arr[right] >= arr[pivot]:
            right-=1
        #left 와 right의 index 번호가 역전 되었을때 pivot과 right값을 교체한다
        if left > right:
            arr[right], arr[pivot] = arr[pivot] , arr[right]
        #아닐경우 각 index를 swap 한다.
        else:
            arr[right], arr[left] = arr[left], arr[right]
    qsort(arr, start, right-1)
    qsort(arr, right+1, end)

#계수 정렬 O(N+K)  N = 데이터의 개수 K = 데이터의 최댓값 크기
#데이터의 크기가 한정되었다면 제일 빠르다
#그러나 데이터의 최대값 기준으로 배열을 만들기 때문에 최대값이 매우크면
# 공간복잡도 면에서 비효율적이다. 
def count_sort(arr):
    count = [0] * (max(arr)+1)

    for i in range(len(arr)):
        count[arr[i]] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ')


#순차 탐색 
def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i+1 #현재 위치 반환

#이진 탐색
#이미 정렬이 완료 된 경우에 효율적
def b_search(arr, target, start, end):
    if start > end:
        return False
    mid = start // end
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        b_search(arr, target, start, mid-1)
    else:
        b_search(arr, target, mid+1, end)
    
#sys 사용하기
#import sys 
#sys.stdin.readline().rstrip()


        
