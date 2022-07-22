from collections import Counter
N = int(input())
arr = [int(input()) for i in range(N)]
sum = 0
for i in range(N):
    sum += arr[i]
arr2 = sorted(arr)
a = sum / N
cnt = Counter(arr2).most_common() #dict형으로 빈도수 나타내줌

print(round(a)) 
print(arr2[N//2])
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])
print(max(arr) - min(arr))


# def di(word):
#     cnt = {}
#     for letter in word:
#         if letter not in cnt:
#             cnt[letter] = 0
#         cnt[letter] += 1
#     return cnt
