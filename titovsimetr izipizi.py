from itertools import permutations
from math import *
from sympy import Matrix, pprint
from random import randint
#x1^3x2+x1^3x3+x1x2^3+x1x3^3+x2^3x3+x2x3^3

class chlen:
    numx = 1
    def __init__(self, ratio = 1, *degree):
        self.ratio = ratio
        self.degree = degree

class mnogochlen:
    pass

n = int(input("Введите количество переменных: "))
perem = ""
for i in range(1, n+1):
    perem += 'x' + str(i) + ', '
perem = perem[:-2]

data = input(f"Введите симметрический мн-н f({perem}):\n").replace(' ','').replace('-','+-').split('+')
for e, i in enumerate(data):
    mass = [1]+[0]*(n)
    nums = i.split('x')
    if nums[0]=='-': mass[0]= -1
    elif nums[0]!='': mass[0] = float(nums[0])
    for j in nums[1:]:
        g = j.split('^')
        if len(g)==1:
            mass[int(g[0])]+=1
        else:
            mass[int(g[0])]+=int(g[1])

    data[e] = mass

newdata = []
for i in data:
    flag = True
    for j in newdata:
        if i[1:] == j[1:]:
            j[0]+=i[0]
            flag = False
            break
    if flag: newdata.append(i)
print(newdata)
data = newdata
#Проверка на симм-ть
flag = True
for a in range(1, n+1):
    if flag:
        for b in  range(a+1, n+1):
            for i in data:
                perest = i.copy()
                perest[a],perest[b] = perest[b],perest[a]
                flag2 = False
                for j in data:
                    if j == perest:
                        flag2 = True
                        break
                if not flag2:
                    flag = False
                    break
if not flag:
    raise ValueError("Этот мн-н не является симметрическим!")


sumi=0
maxi=-1
ind=[]
strsu=''
masmax=[]
strmasmax=[]
strmax=[]
promrez=[]
strkf=[]
rez=[]
kfmax=[]
znach=[]
k=0
indm=[]
for i in range(0,len(data)):
    for j in range(len(data[i])-n,len(data[i])):
        sumi+=data[i][j]
        strsu+=str(data[i][j])
    if sumi>=maxi:
        maxi=sumi
        indm.append(i)
        strmasmax.append(strsu)
        strkf.append(data[i][0])
        masmax.append(sumi)
    sumi=0
    strsu=''
print(strmasmax) # массив выбора лексикографического максимума из кф
for i in range(0,len(strmasmax)):
    if masmax[i]==maxi:
        strmax.append(strmasmax[i])
        kfmax.append(strkf[i])

kfmax=kfmax[strmax.index(max(strmax))]
indm=indm[strmax.index(max(strmax))]
print(indm)
strmax=int(max(strmax))
print(strmax)
print('множитель наибольшего лексикографического набора степение:',kfmax) #  множитель наибольшего лексикографического набора степение= l
print('сумма наибольшего набора l: ',maxi)
# ищем из степеней чья суммма равна максимуму наибольшую  лексикографическую

for i in range(1,strmax+1):
    p=0
    po=[]
    prosh=0
    if len(str(i))==len(str(strmax)):
        for l in range(1,len(data[indm])-1):
                po.append(int(str(i)[prosh:prosh+len(str(data[indm][l]))]))
                prosh=len(str(data[indm][l]))
        po.append(int(str(i)[-len(str(data[indm][-1]))]))
    p=sum(po)

    if p==maxi:
        t=True
        for z in range(1,len(po)):
            if po[z-1]<po[z]:
                t=False

        if t:
            promrez.append(po)

q=[]
otv=[]
print('таблица по лексикографическому возростанию  степеней с максимальной суммой: \n',promrez)# таблица по лексикографическому возростанию  степеней с максимальной суммой обозначим k1...kn
strpromrez=[]

# тогда каждому набору k1<=k2<=...<=kn , будет соответствовать многочлен q1^kn-kn-1...qn-1^k2-k1qn^k1
for i in range(0,len(promrez)):
    for j in range(0, len(promrez[i])-1):
            q.append(int(promrez[i][j])-int(promrez[i][j+1]))

    q.append(int(promrez[i][-1]))
    otv.append(q)
    q=[]
print('вычисленные многочлены: ',otv) # вычисленные многочлены
# функция создает массив соответсующий элементарному симетрическому многочлену с заданым кол-вом перменных
def simetr(n, k):
    nums = [1] * n + [0] * (k - n)
    perm_set =list(set(permutations(nums, k)))


    return perm_set





xmas=[]

spis=[]
sumsi=[]
znachf=[]
# создаем нужное нам кол-во подстановок
for j in range(0,len(otv)):
    for i in range(0,n-1):
        xmas.append(1)

    while len(xmas)<n:
        xmas.append(j)

    # вычислям подстановку xmas во все элементарные
    for z in range(0,n):
        sumsi=simetr(z+1,n)
        sumsumsi=0
        for c in range(0,len(sumsi)):
            proizv=1
            fl=False
            for r in range(0,n):
                spis.append(sumsi[c][r])
                if sumsi[c][r]==1:
                    spis[r]=xmas[r]
                    proizv*=spis[r]
                    fl=True
            if fl:
                sumsumsi += proizv


            spis=[]

        znach.append(sumsumsi)

    sumf=0
    # подстановка xmas в начальную f
    for f in range(0,len(data)):
        proizvf=data[f][0]
        flf=False
        for fin in range(1,len(data[0])):
            proizvf*=xmas[fin-1]**data[f][fin]
            flf=True
        if flf:
            sumf+=(proizvf)
    znachf.append(sumf)
    xmas = []
print('значние q после подостоновки :',znach)
print('значение f после подстановки:',znachf)
znachfdegr=[]
znfhel=[]
znachdegre=[]
znhel=[]
for l in range(0,len(znach)+1-n,n):
    for i in range(len(otv)-1,-1,-1):
        znproizv=1
        for j in range(0,n):
            znproizv*=znach[j+l]**otv[i][j]

        znachdegre.append(znproizv)

        znhel=[]
    znachfdegr.append(znachdegre)
    znachdegre=[]
print('значение -  ',znachfdegr)

matr = znachfdegr
for e, i in enumerate(matr):
    matr[e] = i[1:]+[1]+[znachf[e]-i[0]]
print(matr)
matr = Matrix(matr)
pprint(matr)
matr = matr.rref()[0]
pprint(matr)
m = matr.col(-1)
matr = []
for i in m:
     matr.append(i)

print(matr)
if kfmax!=1:
    print(f'{kfmax:.2f}'.rstrip('0').rstrip('.'),end='')
for i in range(0,n):
    if otv[-1][i]!=0:
        print(f'q{i+1}^{otv[-1][i]:.2f}'.rstrip('0').rstrip('.'),end='')
print('',end='')
if len(otv)>1:
    for t in range(len(otv) - 2, -1, -1):
        if matr[(len(matr)-t)-2] != 0:
            if matr[(len(matr)-t)-2]>0:
                print(f'+{matr[(len(matr)-t)-2]:.2f}'.rstrip('0').rstrip('.'),end='')
            else:
                print(f'{matr[(len(matr)-t)-2]:.2f}'.rstrip('0').rstrip('.'), end='')
        for z in range(0,n):
            if matr[(len(matr) - t) - 2] != 0:
                if otv[t][z]!=0:
                    print(f'q{z+1}^{otv[t][z]:.2f}'.rstrip('0').rstrip('.'),end='')
if(matr[-1]!=0):
    if(matr[-1]>0):
        print('+',end='')
    print(f'{matr[-1]:.2f}'.rstrip('0').rstrip('.'))


