#실습1
sentence=input("문장을 입력하세요.")
count=sentence.count(' ')
sentence=sentence.replace(' ','\n')
print(sentence)
print("(총", count+1, end='')
print('단어)')
#실습2
number=int(input("숫자를 입력하세요(1-10000) : "))
numbers=[]
while True:
    numbers.append(number)
    for i in numbers:
        print("+", end='')
        print("%4d"%i)
    ssum=sum(numbers)
    print("=", end='')
    print(ssum)
    number=int(input("숫자를 입력하세요(1-10000) : "))
#실습3
mathexp=input('수식을 입력하세요.')
components=mathexp.split('+')
ssum=0
for i in components:
    ssum=ssum+int(i)
print('합계는', ssum)