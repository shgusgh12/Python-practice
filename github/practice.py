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

#반대로 출력시 lst[처음인덱스:어디까지출력할건지:출력방향및간격 :]
for i in lst[0:3:1]:
    print(i, end=' ')