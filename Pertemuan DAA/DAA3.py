import pandas as pd
import numpy as np
## -----------------aLIST-----------------
print("\n===============================")
aList = ['John', 33, 'Fredi', True]

print(aList)
print("===============================")

## -------------LIST MAHASISWA-------------
print("\n===============================")
mahasiswa = ['Aldho Sukadi', '2020071048', 'Informatika', 'DAA', '9-15-2021', 'Universitas Pembangunan Jaya']

print(mahasiswa[0])
print(mahasiswa[1:4])
for loopMahasiswa in mahasiswa:
    print("UPJ " + loopMahasiswa)
print("===============================")

## -------------LIST BIN COLOR-------------
print("\n===============================")
bin_colors = ['Red', 'Green', 'Blue', 'Yellow']

print(bin_colors[1])
print(bin_colors[2:], "\n")

for aColor in bin_colors:
    print(aColor)
print("===============================")

## ---------------UPJ TUPLE---------------
print("\n===============================")
UPJ = ('Universitas', 'Pembangunan', 'Jaya')

print(UPJ)
print("===============================")

## --------------NESTED TUPLE--------------
print("\n===============================")
## cara pertama 
pertama = (100)
kedua   = (200, 400, 600)
ketiga  = (300)
keempat = (400, 800)
nested_tuple1 = ((pertama, ) + (kedua, )+ (ketiga, ) + (keempat, ))
print(str(nested_tuple1))

## Cara kedua
nested_tuple2 = ((100), (200, 400, 600), (300), (400, 800))
print(nested_tuple2)
print("===============================")

## ----------DICTIONARY BIN COLORS----------
print("\n===============================")
bin_colors = {
    "manual_color": "Yellow",
    "approved_color": "Green", 
    "refused_color": "Red"
}
print(bin_colors["approved_color"])

bin_colors['approved_color'] = "Purple"
print(bin_colors)

print("===============================")

## ------LATIHAN DICTIONARY MAHASISWA--------
print("\n===============================")
dataMahasiswa = {
    "NIM"    : "2020071048",
    "Nama"   : "Aldho Sukadi", 
    "Prodi"  : "Informatika",
    "Univ"   : "Universitas Pembangunan Jaya"
}
print(dataMahasiswa["NIM"], dataMahasiswa["Nama"], dataMahasiswa["Prodi"], dataMahasiswa["Univ"])
print("===============================")

## ----------------SETS PLANTS---------------
print("\n===============================")
green1 = {'grass', 'leaves'}
print(green1)

green2 = {'grass', 'leaves', 'leaves'}
print(green2)
print("===============================")

## ----------------LATIHAN SETS----------------
print("\n===============================")
yellow = {'dandelions', 'fire hydrant', 'leaves'}
red = {'fire hydrant', 'rose', 'blood', 'leaves'}
print(yellow | red)
print(yellow & red)
print("===============================")

## --------------DATA FRAME PANDAS-------------
print("\n===============================")
df = pd.DataFrame([
    ['1', 'Fares', '32', True],
    ['2', 'Elena', '23', True],
    ['3', 'Steven', '40', True]
])
df.columns = ['id', 'name', 'age', 'decision']
print(df)
print("\n")
print(df[['name', 'age']])
print("\n")
print(df.iloc[:,3])
print("===============================")

## ----------LATIHAN DATA FRAME PANDAS---------
print("\n===============================")
mhs = pd.DataFrame([
    ['1', 'Informatika', '50', '30', '20'],
    ['2', 'Sistem Informasi', '55', '30', '25'],
    ['3', 'Teknik Sipil', '40', '30', '10']
])
mhs.columns = ['No', 'Prodi', 'Mahasiswa', 'Laki-Laki', 'Perempuan']
df_reset=mhs.set_index('No')
print(mhs)
print("\n")
print(mhs[['No', 'Prodi', 'Perempuan']])
print("===============================")

## ------------------MATRIX-------------------
print("\n===============================")
myMatrix = np.array([
    [11, 12, 13],
    [21, 22, 23],
    [31, 32, 33]
])
print(myMatrix)
print("\n")
print(type(myMatrix))
print("===============================")

## ------------------STACK-------------------
print("\n===============================")
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

stack = Stack()
stack.push('Red')
stack.push('Green')
stack.push('Blue')
stack.push('Yellow')

print(stack.pop())

print(stack.isEmpty())
print("===============================")

## ------------------QUEUE-------------------
print("\n===============================")
class Queue(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

queue = Queue()
queue.enqueue('Red')
queue.enqueue('Green')
queue.enqueue('Blue')
queue.enqueue('Yellow')

print(queue.size())

print(queue.dequeue())
print(queue.dequeue())
print("===============================")