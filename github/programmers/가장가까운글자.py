def solution(s):
    arr = [] 
    answer = [-1] * len(s)
    for i in range(len(s)):
        arr.append(ord(s[i]))
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and j > i:
                if arr[i] == arr[j]:
                    answer[j] = j - i
                
    return answer
