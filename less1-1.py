import pymystem3
from  pymystem3 import Mystem

tt = 'Простая проверочка лемматизации русского текста на вскидку'
m = Mystem()
lem = m.lemmatize(tt)


print('Старт')
rr='Самый крутой тест'

print(rr)
print( lem)


