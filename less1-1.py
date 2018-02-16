import pymystem3
from  pymystem3 import Mystem
file = open('texts.txt','r', encoding='utf-8')
ttt = file.read()

m = Mystem()
lem = m.lemmatize(ttt)


print('Старт')
rr='Самый крутой тест'

print(ttt)
print( lem[15:280])

print(' tktjhfnlfnkfj jf kljfhlf l')
