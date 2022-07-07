import sys
input = sys.stdin.readline

n = int(input())
arr=[]
for i in range(n):
    [x, y] = map(int, input().split())  #map 함수 이용해서 배열에 여러개 입력받기
    arr.append([x,y]) #2차원 배열생성  

arr2 = sorted(arr) 
    
for i in range(n):
    print(arr2[i][0],arr2[i][1]) 

