from operator import concat


a = 100, 5 , 'k'
print('"더이상 카레먹기 싫어요"')
#is 연산자 
#== 연산자는 값을 비교하는 연산자
#값을 비교하는 것이 아니라 변수가 가리키고 있는 곳 비교
a = [1,2,3,4,5]
b = a
c = [1,2,3,4,5]

print('a is b = ', a is b)
print('a is c= ', a is c)
print('b is c = ',b is c)
a = "korea"
b += "!"
c = b[:-1]
#슬라이싱 하는 순간 새롭게 할당된다.
print ('a is c =', a is c)

#elif else 조건문 
age = 20

if age < 30:
    print("청년이에요")
elif age < 60:
    print("중년")
else:
    print("노년")

#for 반복문
for asdf in range(10):
    print(asdf)

#이중 for문 별찍기

for i in range(10,0,-1):
    for j in range(i):
        print("*", end='')
    print("")


#리스트 end 옵션에 \t 추가하면 tab 된 상태로 출력
lst = ['A','B','C','D','E']
for i in range(len(lst)):
    print(lst[i], end='\t')
print("")

# #반대로 출력시 lst[처음인덱스:어디까지출력할건지:출력방향및간격 :]
# for i in lst[0:3:1]:
#     print(i, end=' ')

#리스트 안의 리스트 값 출력
a = [100, 3.14, 'korea', [100, 200,300], (100, 200 ,300)]
print(a[4][2])

for i in range(len(a)):
    print(a[i], end=' ')
print()


#정렬 sort() 함수 사용
b = [4,2,5,2,4]
# b.sort(reverse=True) #내림차순
# for i in range(len(b)):
#     print(b[i])

for i in range(-4, -1):
    print(b[i])

#리스트에 추가 삭제
b.append(1)
for i in range(len(b)):
    print(b[i], end=' ')
print()
del b[-1]
for i in range(len(b)):
    print(b[i], end=' ')
print()

# #리스트 병합  더하기 연산자 튜플도 가능
# a = [0,1,2,3,4]
# b = [5,6,7,8,9] 
# print(a*3)

# animals = ['elephant', 'hippo','lion','tiger','alligator']
# name = input('동물의 이름을 입력하시오 ')
# index = animals.index(name)
# print(f'{name} 동물의 케이지는 {index}번 위치에 있습니다')

#중복 제거
lst = [1,2,3,4,6,7,7,7]
lst2 = set(lst)
lst3 = list(lst2)
print(lst3, type(lst3))

#list comprehension
b = []
for i in range(1,11):
    b.append(i)

c = [i*i for i in range(1,11)]
print(c)
c = [i*i for i in range(1,11)if i!= 5]
print(c)
c = [i for i in range(1,51)if i%2 != 0]
print(c)

def func(i):
    i = i*2
    return i
c = [func(i) for i in [1,2,3,4,5]]
print(c)