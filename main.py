# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class Student:
    def __init__(self, python_skill=0):
        self.python_skill = python_skill

    def get_python_skill(self):
         return self.python_skill

    def learn_python(self):
        self.python_skill = self.python_skill + 1

s = Student()
s.get_python_skill()
s.learn_python()
s.get_python_skill()

'''
class ComplexNumber:
    def __init__(self, a=0,b=0):
        self.a = a
        self.b = b
    def __add__(self, other): #сложение
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __mul__(self, other): #умножение
        return ComplexNumber(self.a*other.a - self.b*other.b, self.b*other.a + self.a*other.b)

    def __eq__(self, other): #сравнение ==
        if self.a == other.a and self.b == other.b: return True
        else: return False

    def show(self):
        print(str(self.a) + ' +' + str(self.b) + 'i')

a = ComplexNumber(10, 20)
b = ComplexNumber(30, 40)
c = ComplexNumber(40, 60)

f = a*b
f.show()
print(a+b == c)
'''
'''
from itertools import count
class PrimesIterator:

    def __init__(self, start_num=2):
        self.start = start_num

    def __iter__(self):
        return self

    def __next__(self):
        for i in count(self.start): #от заданного числа и до бесконечности
            prime = True
            for j in range(2, i): #по всем числам от 2 до i не включая его
                if i % j == 0:
                    prime = False
            if prime:
                self.start = i + 1
                return i

c = PrimesIterator(50)
print(next(c))
print(next(c))
print(next(c))
'''

#for i in PrimeNumbers(10):
#     print(i)
"""

def get_full_help(obj):
    for name in dir(obj):
        attr = getattr(obj, name)
        if callable(attr) and "_" not in name:
            doc = attr.__doc__
            small_help = doc.split('\n')[0]
            print(f'{name:<15}{small_help}')


class C:
    __a = 42
c = C()

print(c._C__a)
"""
"""
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""
'''
import os
import sys
import itertools
import re

def project_stats(path, extensions):
    """
    Вернуть число строк в исходниках проекта.

    Файлами, входящими в проект, считаются все файлы
    в папке ``path`` (и подпапках), имеющие расширение
    из множества ``extensions``.
    """
    dir_list = list(map(lambda x: x[0],os.walk(path)))
    #print(dir_list)
    filter_list = list(map(iter_filenames,dir_list))
    filter_list  = (','.join(map(','.join,filter_list))).split(',')
    #print(filter_list)
    filter_list = with_extensions(extensions,filter_list)

    return total_number_of_lines(filter_list)


def total_number_of_lines(filenames):
    """
    Вернуть общее число строк в файлах ``filenames``.
    """
    return sum(map(lambda x: number_of_lines(x),filenames))


def number_of_lines(filename):
    """
    Вернуть число строк в файле.
    """
    return sum(1 for line in open(filename, 'r'))

#def get_dirs(path):
#    list(filter(lambda x: os.path.isdir(path + x), os.listdir(path)))

def iter_filenames(path):
    """
    Итератор по именам файлов в дереве.
    """

    #flist = os.listdir(path)
    #dirs = list(filter(lambda x: os.path.isdir(path +  x), flist))
    #print(list(filter(lambda x: os.path.isfile(x), list(map(lambda x: path+x,flist)))) )
    #flist = list(filter(lambda x: os.path.isfile(x), list(map(lambda x: path+x,flist)))) + list(map(iter_filenames,list(map(lambda x: path+x+'/', dirs))))
    #string = str(','.join(flist))
    return list(map(lambda x: path+x,os.listdir(path)))
    #return list(filter(lambda x: os.path.isfile(x), list(map(lambda x: path+x,os.listdir(path)))))


def with_extensions(extensions, filenames):
    """
    Оставить из итератора ``filenames`` только
    имена файлов, у которых расширение - одно из ``extensions``.
    """
    return list(filter(lambda x: get_extension(x) in extensions,filenames))


def get_extension(filename):
    """ Вернуть расширение файла """

    return re.findall('(\.[a-zA-z]+)?$',filename)[0]


def print_usage():
    print("Usage: python project_sourse_stats_3.py <project_path>")


#if __name__ == '__main__':
#    if len(sys.argv) != 2:
#        print_usage()
#        sys.exit(1)
#
project_path = sys.argv[1]
print(project_stats(project_path, {'.py'}))

#project_path = '/home/senator/work/python/education/'
#print(list(os.walk(project_path)))
#print(project_stats(project_path, {'.py'}))
#print(total_number_of_lines(['/home/senator/work/python/education/main.py','/home/senator/work/python/education/main.py']))
#print(with_extensions({'.py'},['/home/senator/work/python/education/main.py','/home/senator/work/python/education/venv']))
#print(get_extension('aaa'))

'''
'''

import re

def check_r(string):
    temp = re.findall("rgb\(([0-9]+),([0-9]+),([0-9]+)\)", string)

    if len(temp) > 0: #find!
        for val in temp[0]:

            if int(val) > 255 or int(val) < 0:
                return False
                break
        return True

    temp = re.findall("rgb\(([0-9]+)%,([0-9]+)%,([0-9]+)%\)", string)

    if len(temp) > 0: #find!
        for val in temp[0]:
            if int(val) > 100 or int(val) < 0:
                return False
                break
        return True

    temp = re.findall("rgba\(([0-9]+),([0-9]+),([0-9]+),[0-9,.]*\)", string)

    if len(temp) > 0: #find!
        for val in temp[0]:
            if int(val) > 255 or int(val) < 0:
                return False
                break
        temp = re.findall("rgba\([0-9]+,[0-9]+,[0-9]+,([0-9,.]*)\)", string)

        if float(temp[0]) < 0 or float(temp[0]) > 1: return False

        return True

    return False #end of func, no matches

string = str(input())

print(check_r(string))
'''


"""
import re

def check_pass(str):
    if len(str) < 6 or len(str) > 12: return False
    if len(re.findall("[a-z]",str)) < 1: return False
    if len(re.findall("[0-9]",str)) < 1: return False
    if len(re.findall("[A-Z]", str)) < 1: return False
    if len(re.findall("[^0-9a-zA-Zа-яА-ЯёЁ]", str)) < 1: return False #спец символ
    return  True

string = str(input())

print(check_pass(string))
"""
#print(len(re.findall("[a-zA-Zа-яА-ЯёЁ]",string)))
#print(len(re.findall("\d",string)))
#print(len(re.findall("[^0-9a-zA-Zа-яА-ЯёЁ]",string)))


"""
d = {'X':10,'XX':20,'XXX':30,'XL':40,'L':50,'LX':60,'LXX':70,'LXXX':80,'XC':90,'I':1,'II':2,'III':3,'IV':4,'V':5,'VI':6,'VII':7,'VIII':8,'IX':9,'C':100,'CC':200,'CCC':300,'CD':400,'D':500,'DC':600,'DCC':700,'DCCC':800,'CM':900,'M':1000,'MM':2000,'MMM':3000}


sum=0
string = str(input())
for key in sorted(d, key=len,reverse=True): #возвращает только ключи от словаря, но в порядке уменьшения длины строки
    if string.count(key) > 0:
        #print(key)
        sum = sum + string.count(key)*d[key]
        string = string.replace(key,'')
print(sum)
"""
"""
from collections import Counter
string = Counter(str(input()))
min=len(string)
max=-1
for key in string:
    if string[key] > max: max = string[key]
    if string[key] < min: min = string[key]

if max == min:
    print(True) #точно да
elif max > min + 1:
    print(False) #точно нет
else:
    #смотрим сколько таких элементов
    k = 0
    for key in string:
        if string[key] == max:
            k=k+1
        if k > 1: break;

    if k > 1: print(False)
    else: print(True)

"""
"""

string = str(input())

temp=[]
sub_str = []
for let in string:
    if let not in temp: #подстрока идет
        temp.append(let)
    else: #подстрока кончилась
        if ''.join(temp) not in sub_str: #такой еще не находили
            sub_str.append(''.join(temp))
        temp=[]
        temp.append(let)
if ''.join(temp) not in sub_str:  # такой еще не находили
    sub_str.append(''.join(temp))

dict=[]

for strr in sub_str:
    dict.append([len(strr),strr])



if max(dict)[0] == dict[0][0]: #max равен первому
    print(dict[0][1])
else: print(max(dict)[1])
"""
"""
from collections import Counter
string = Counter(str(input()))
output=""
for key in string:
    output = output + key
print(output)
"""
"""
words = str(input()).split(' ')

max_len = len(max(words, key=len)) #нашли самое длинное слово

for str in words: #выводим первое
    if len(str) == max_len:
        print(str)
        break
"""
"""

numbers = str(input()).split(' ')
array = []
def is_int(n):
    return int(n) == float(n)

for s in numbers:
    if s != '0': array.append(int(s))

def mean_ar(*args):
    temp = sum(list(map(int, args[0])))/len(args[0])
    if is_int(temp): return int(temp)
    else: return temp

print(mean_ar(array))
"""

"""
words = str(input()).split(' ')
numbers = str(input())


dict = {1:['.', ',', '-'],2:['а',"б","в","г"],3:["д","е","ж","з"],4:["и","й","к","л"],5:["м","н","о","п"],6:["р","с","т","у"],7:["ф","х","ц","ч"],8:["ш","щ","ъ","ы"],9:["ь","э","ю","я"]}

final=[]
flag_pass = False
len_num = 0
for n in range(len(numbers)): #столько раз, сколько клавиш ввели
   len_num = int(numbers[n])
   for string in words:
       flag_pass = False
       for let in dict[len_num]:
           if string[n].lower() == let: flag_pass = True # перебрали все буквы от этой кнопки, если она совпала со своим значением в слове - тру

       if flag_pass == False:
           words.remove(string)

print(" ".join(words))
"""

'''
string = str(input())

dict = {'А': 'A', 'а': 'a','Ж': 'Zh', 'ж': 'zh','Н': 'N', 'н': 'n','Ф': 'F', 'ф': 'f','Ъ': 'Ie', 'ъ': 'ie',  'Б': 'B', 'б': 'b','З': 'Z', 'з': 'z','О': 'O', 'о': 'o','Х': 'Kh', 'х': 'kh','Э': 'E', 'э': 'e',  'В': 'V', 'в': 'v','И': 'I', 'и': 'i','П': 'P', 'п': 'p','Ц': 'Ts', 'ц': 'ts','Ю': 'Iu', 'ю': 'iu',  'Г': 'G', 'г': 'g','Й': 'I', 'й': 'i','Р': 'R', 'р': 'r','Ч': 'Ch', 'ч': 'ch','Я': 'Ia', 'я': 'ia',  'Д': 'D', 'д': 'd','К': 'K', 'к': 'k','С': 'S', 'с': 's','Ш': 'Sh', 'ш': 'sh','ь': '', 'Е': 'E', 'е': 'e','Л': 'L', 'л': 'l','Т': 'T', 'т': 't','Щ': 'Shch', 'щ': 'shch',  'Ё': 'E','ё': 'e','М': 'M', 'м': 'm','У': 'U', 'у': 'u','Ы': 'Y', 'ы': 'y'}

for char in dict:
    string = string.replace(char, dict[char])

print(string)
'''
'''
string = str(input()).lower().split(' ')
string.sort()

temp=''
temp2=''
for word in string:
    temp = list(word)
    temp.sort()
    for fi in string:
        if fi == word: continue
        temp2=list(fi)
        temp2.sort()

        if temp == temp2:
            print(word + ' ' + fi)
            string.remove(fi)
            break
'''
'''
string = str(input()).lower()
string = string.split(' ')

array = []

for word in string:
    if word in array: continue
    else: array.append(word)

print(" ".join(array))
'''
"""
import re
from collections import OrderedDict

string = str(input()).lower()

string = re.sub("[^a-zA-Zа-яА-ЯёЁ]",'',string)

dict = {}

for char in string:
    if dict.get(char,'') == '': dict[char] = 1
    else: dict[char] += 1

for char in sorted(dict.keys()):
    print(char + ' ' + str(dict[char]))
"""
"""
string = str(input())

a = ''
i = 0
for n in range(len(string)):
    if n+1 < len(string):
     if string[n] == string[n+1]:
         i=i+1
         continue
    a = a + string[n] + str(i+1)
    i=0

print(a)
"""
'''
import re

string = str(input())

print(len(re.findall("[a-zA-Zа-яА-ЯёЁ]",string)))
print(len(re.findall("\d",string)))
print(len(re.findall("[^0-9a-zA-Zа-яА-ЯёЁ]",string)))
'''
'''
com_number = str(input())

if len(com_number)>2: com_number = int(str(com_number)[len(com_number)-2] + str(com_number)[len(com_number)-1])
else: com_number = int(com_number)

if 10 < com_number < 20: print('комментариев')
elif str(com_number)[-1] == '1': print('комментарий')
elif 1 < int(str(com_number)[-1]) < 5: print('комментария')
else: print('комментариев')
'''

'''
str1 = str(498578324323)
summ = 0
while len(str1) > 1:
    for i in str1:
        summ = summ + int(i)
    str1 = str(summ)
    summ = 0

print(str1)


fib_n = 0
fib_nn = 1
i=0

while i<8:
    fib_nnn = fib_n + fib_nn
    fib_n = fib_nn
    fib_nn = fib_nnn
    i += 1

print(fib_n)

s = 'ababaakd30023aaaa'
uniq = ''

for i in s:
    if i not in uniq:
        uniq+= i

freq = 0
max = ''
for i in uniq:
    if freq < s.count(i):
        freq = s.count(i)
        max = i

print(max)






print(2 ** 1024)

объем_океана_м3 = 1340.74 * (10 ** 6) * (10 ** 9)

масса_океана_тонны = объем_океана_м3 * 1.024

масса_золота_г = масса_океана_тонны * 0.005 * (10 ** -3)

ребро = (масса_золота_г * (10 ** -6) / 19.32) ** (1. / 3.)

print(ребро)

print(sum(range(1, 10)))
print(sum(range(1, 100)))
print(sum(range(1, 1000)))
print(sum(range(1, 10000)))
print(sum(range(1, 100000)))

messages = "это тестовое сообщение"
print(messages.title())

s = 'a'
s = s + 'b'
print(s)
s = s + 'c'
print(s)

s = 'test'
space = ' '
for i in s:
    print(space + s)
    space = space + ' '

'''