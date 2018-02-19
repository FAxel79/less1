import math
import pymorphy2
import re

file = open('texts5.txt','r', encoding='utf-8')
ttt = file.read()
file.close()
m = pymorphy2.MorphAnalyzer()

# start
# Очистка списка от мусора
def clerit (input_list):

    Stop_In_Word_List = [' ', '.', ',', '!', '?', ':', ';', '+', '. ', ', ', '\n', '(', ')', ' (', ') ', ': ', '-', ')\n', ':\n', ' - ', '.\n\n']
    outp = []
    for i in input_list:
        if i in Stop_In_Word_List:
            pass
        else:
            if i.isalnum():
                outp.append(i)
    return outp
# подсчет вхождений и их мест
def counN (inp,inn):
    nnom = []
    outp = inp.count(inn)
    if not outp:
        outp =0
    nnom.append(outp)
    j = 0
    if isinstance(inp, list):
        for i in range (outp):
            k = inp.index(inn,j)
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

#Подсчет DTF
def Set_DTF (CLemma_list):
    OutDict = {}
    WorkSet=()
    WorkSet= set(CLemma_list)
    NCount = len(CLemma_list)
    for Wor in WorkSet:
        OutDict[Wor]=math.sqrt((CLemma_list.count(Wor)*100)/math.log(NCount,2))
    return OutDict

def SortMy2 (ItemL):
    return ItemL[2]

def Wegh (CWInLem, Wor):

    We= (CWInLem) * 100 /math.log (MyDict_TDF[Wor],7)

    We = CWInLem**1.35/(3- (math.log(math.fabs(CWInLem/MyDict_TDF[Wor]**2),2)))
    return We

print('Старт')
rr='Самый крутой тест'



#print(ttt)
#print( lem[15:280])
Text_split = re.split(r'(\W+)', ttt)
All_Lemma_list =[]
for One_word in Text_split:
    All_Lemma_list.append(m.parse(One_word)[0].normal_form)
Clear_Leemma_List = clerit(All_Lemma_list)
#Лемматизировали и почистили


print(Clear_Leemma_List)
Input_word= ''
Set_Word_Around = set()
MyDict_TDF = Set_DTF(Clear_Leemma_List)
Input_word = []
while Input_word != '1':
    Input_word = input().split()[0]
    Input_Lemma = m.parse(Input_word)[0].normal_form

    print(str(Input_Lemma) + ' в тексте с количеством словарных единиц: ' + str(len (Clear_Leemma_List)))
    Namber_Lemm_in_Text_and_Position = counN(Clear_Leemma_List, Input_Lemma)
    try:
        print(str(Namber_Lemm_in_Text_and_Position) + '   процент: ' + str(MyDict_TDF[Input_Lemma]))
    except KeyError:
        print(" Не вошло в текст")
    Word_Around_List = []
    for x in range(len(Namber_Lemm_in_Text_and_Position) - 1):
        Diapozon=12  # Берем по N слов вокруг

        Fainded_Words = findnear(Namber_Lemm_in_Text_and_Position[x + 1], Diapozon, -1, Clear_Leemma_List)
        for Word in Fainded_Words:
            Word_Around_List.append(Word)
        Fainded_Words = findnear(Namber_Lemm_in_Text_and_Position[x + 1], Diapozon, 1, Clear_Leemma_List)
        for Word in Fainded_Words:
            Word_Around_List.append(Word)

    Set_Word_Around = set(Word_Around_List)
    # Найденные слова без повторных вхождений
    Temp_List = []
    #Dict = {}
    All_Weght = 0
    for Word_in_Set in Set_Word_Around:
        Count_Word_Around = Word_Around_List.count(Word_in_Set)
        Weght = Wegh(Count_Word_Around,Word_in_Set)
        Temp_List.append([Word_in_Set,Count_Word_Around,Weght])
        All_Weght= All_Weght+Weght

    print(All_Weght)
    Temp_List.sort(key = SortMy2, reverse=True)
    for iu in Temp_List:
        if len(iu[0])>2:
            print(iu)

    print(Namber_Lemm_in_Text_and_Position[0]*All_Weght)
    #print(MyDict_TDF)
