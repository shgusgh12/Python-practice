from email.quoprimime import body_check
from operator import concat
from winreg import HKEY_CURRENT_CONFIG


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

#중첩 반복문 튜플로 묶어라 하나의 값은 안묶어도 된다
a = [(i, j) for i in range(1,3) for j in range(1,10)]
print(a)

#딕셔너리 인덱스 접근 불가능
b = {}
b['id'] ='hong'
b['id'] = 'kim' #나중에 들어온 key값으로 대체됨
b['name']= '홍길동'
b['age'] = 20
b['address'] = (1,4,2,4) #리스트도 가능
print(b)
#key값만 출력
for i in b.keys(  ):
    print(i, end=' ')
print()
#value만 출력
for i in b.values():
    print(i, end=' ')
print()
#key, value 모두 출력 ====> tuple로 묶인다
for i in b.items():
    print(i , type(i))
#key가 인덱스의 역할을 한다
print(b['id'])
#중첩 dictionary
b2 = {
    'name' : 'jake',
    'age' : 30,
    'pastime' : {
        'reading': 30,
        'walking': 60
    }
}
print(b2['pastime']['walking'])
#삽입 
b2['age'] = 30
print(b2['age'])
#삭제 
del b2['age']
print(b2)

# print('이름을 입력하세요: ', end='')
# name = input()
# print(f'안녕하세요? {name}님')

# n = int(input())
# i = 1
# sum = 0
# while i <= n:
#     sum += i
#     i = i+1

#튜플 언패킹
fruits = ('apple','banana','grapes')
(mine, *yours)= fruits
print(yours) #yours는 list 형태로 저장된다
#중복허용 안하면서 순서가 중요한경우 set사용 못할때
mylist = ['a','b','c','c','c']
dic = dict.fromkeys(mylist) #value 값들은 전부 none으로 표시됨
print(dic)
mylist = list(dic)
print (mylist)
