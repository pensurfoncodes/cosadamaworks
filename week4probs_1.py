#1번
print('%10s'%'HONG    ')
print('%10.5d'%273)
print('%10s'%'153.288%')
#2번
import random
students=['a', 'b', 'c', 'd', 'e']
for i in students:
    i_kr=random.randint(1,100)
    i_math=random.randint(1,100)
    i_eng=random.randint(1,100)
    print(i, '- 국어:', '%3d'%i_kr, '수학:', '%3d'%i_math, '영어:', '%3d'%i_eng, end='')
    isum=i_kr+i_eng+i_math
    print(' 총합:', '%3d'%isum, end='')
    iavg=isum/3
    print(' 평균: %5.2f'%iavg)
#3번
sentence="Not all that Mrs Bennet however with the assistance of her five daughters could ask on the subject was sufficient to draw from her husband any satisfactory description of Mr Bingley"
sentence_lc=sentence.lower()
print(sentence_lc.count("m"))
words=sentence_lc.split(" ")
words.sort()
line={}
for i in words:
    line[i]=words.count(i)
print(line)
#4번
mathexp=input('수식을 입력하세요:')
mathexp_new=mathexp.replace("-","+-")
components=mathexp_new.split('+')
ssum=0
for i in components:
    ssum=ssum+int(i)
print(ssum)
#5번
self_intro=input('문장을 입력하세요:')
lines=self_intro.split('.')
line=lines[0]
nameline=line.split(' ')
if '합니다' in nameline:
    nearname=nameline[1]
    closename=nameline[1].replace('',' ')
    almostname=closename.split(' ')
    name=[almostname[-7], almostname[-6], almostname[-5]]
    print('이름 :', name[0], end='')
    print(name[1], end='')
    print(name[2])
elif '이름은' in nameline:
    nearname=nameline[2]
    closename=nameline[2].replace('',' ')
    almostname=closename.split(' ')
    name=[almostname[-7], almostname[-6], almostname[-5]]
    print('이름 :', name[0], end='')
    print(name[1], end='')
    print(name[2])
else:
    nearname=nameline[1]
    closename=nameline[1].replace('',' ')
    almostname=closename.split(' ')
    name=[almostname[-7], almostname[-6], almostname[-5]]
    print('이름 :', name[0], end='')
    print(name[1], end='')
    print(name[2])