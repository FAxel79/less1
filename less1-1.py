import pymorphy2
import re

file = open('texts.txt', 'r', encoding='utf-8')
ttt = file.read()
file.close()
m = pymorphy2.MorphAnalyzer()
# lem = m.lemmatize(ttt)
tt = re.split(r'(\W+)', ttt)
for i in tt:
    rr = m.parse(i)[0].normal_form
    print(rr)
rr='Самый крутой тест'
print(ttt)
# print( lem[15:280])
