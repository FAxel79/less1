import pymystem3
from  pymystem3 import Mystem
file = open('texts.txt','r', encoding='utf-8')
ttt = file.read()
file.close()
m = Mystem()
lem = m.lemmatize(ttt)
# start
# Очистка списка от мусора
def clerit (inp):
    sstop = [' ','.',',','!','?',':',';','+','. ',', ','\n','(',')',' (',') ',': ','-', ')\n', ':\n', ' - ']
    outp = []
    for i in inp:
        if i in sstop:
            pass
        else:
            outp.append(i)
    return outp
# подсчет вхождений и их мест
def counN (inp,inn):
    nnom = []
    outp = inp.count(inn[0])
    if not outp:
        outp =0
    nnom.append(outp)
    j = 0
    if isinstance(inp, list):
        for i in range (outp):
            k = inp.index(inn[0],j)
            nnom.append(k)
            j = k+1
    return nnom

#Поиск соседних слов
def findnear (Ind,Col,Nap,Llist):
    pass
    if Nap >0:
        if Ind+Col > len (Llist):
            Col  = len(Llist)-Ind
        Nlist = Llist[Ind+1:Ind+Col+1]

    elif Nap <0:
        if Col > Ind:
            Col = Ind
        Nlist = Llist[Ind-Col:Ind]
    else:
        Nlist = None
    Outer = Nlist
    return  Outer



print('Старт')
rr='Самый крутой тест'



#print(ttt)
#print( lem[15:280])
st = clerit(lem)
print(st)
ss=''
a = set()
while ss != '1':
    ss = input().split()[0]
    ssl = m.lemmatize(ss)
    ssl = clerit(ssl)
    print(str(ssl)+' в тексте с количеством словарных единиц: '+ str(len (st)))
    nn = counN(st,ssl)
    print(str(nn)+'   процент: '+ str(nn[0]*100/len(st)))
    VF = []
    for jj in range(len(nn)-1):
        k=9

        f = findnear(nn[jj + 1], k, -1, st)
        for o in f:
            VF.append(o)
        f = findnear(nn[jj+1],k,1,st)
        for o in f:
            VF.append(o)

    a = set(VF)
    b = []
    q = {}
    for t in a:

        l=VF.count(t)
        q[t] = l
        #print(str(t)+' встретилось раз  '+str(l))
   # print(str(VF))
   # print(str(a))
    for key in q:
        b.append((q[key], key))
        b.sort(reverse=True)
    for fd in b:
        if fd[0]>1 and len(fd[1])>2:
            print (str (fd[0]) +' раз встретилось :  ' + str(fd[1]))