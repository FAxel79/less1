import pymorphy2

file = open('texts2.txt', 'r', encoding='utf-8')
ttt = file.read()
m = pymorphy2.MorphAnalyzer()
# lem = m.lemmatize(ttt)
tt = ttt.split(' ')
for i in tt:
    rr = m.parse(i)[0].normal_form
    print(rr)
rr='Самый крутой тест'
print(ttt)
# print( lem[15:280])
