import numpy as np

## PERTEMUAN DAA YANG KE 2

## Print Hello World
print("\n================================")
print(np.__version__)

print("Hello, World!!")

print("Nama Saya Aldho Sukadi")

print("NIM Saya 2020071048")

print("================================\n")


## if else
print("================================")
if 5 > 2 :
    print("Five Greater than Two!!")

print("================================\n")


## Print Variable
print("================================")
x = 5 
y = "john"

print(x)
print(y)

print("================================\n")

## Print Variable
print("================================")
x = 5 
x = "sally"

print(x)

print("================================\n")

## Notasi Big O
print("================================")
def getFirst(myList):
    return myList[0]

print(getFirst([1,2,3]))

print(getFirst([1,2,3,4,5,6,7]))
print("================================\n")

## Notasi Big O get second
print("================================")
def getSecond(myList):
    return myList[1]

print(getSecond([1,2,3]))

print(getSecond([1,2,3,4,5,6,7]))
print("================================\n")

## Notasi Big O get last
print("================================")
def getLast(myList):
    return myList[-1]

print(getLast([1,2,3]))

print(getLast([1,2,3,4,5,6,7]))
print("================================\n")

## Notasi Big O get sum
print("================================")
def getSum(myList):
    sum = 0 
    for item in myList:
        sum = sum+item
    return sum

print(getSum([1,2,3]))

print(getSum([1,2,3,4,5,6,7]))
print("================================\n")

## Notasi Big O get kali
print("================================")
def getKali(myList):
    kali = 1 
    for item in myList:
        kali = kali*item
    return kali

print(getKali([1,2,3]))

print(getKali([1,2,3,4,5,6,7]))
print("================================\n")

## Notasi Big O get bagi
print("================================")
def getBagi(myList):
    bagi = 100
    for item in myList:
        bagi = bagi/item
    return bagi

print(getBagi([10,5]))

print(getBagi([100,20,5]))
print("================================\n")

## Notasi Big O get bagi 2 himpunan
print("================================")
def getBagi(myList):
    bagi = 100
    for row in myList: 
        for item in row:
            bagi = bagi / item
    return bagi

print(getBagi([[10],[5]]))
print("================================\n")

## Notasi Big O get kurang
print("================================")
def getKurang(myList):
    kurang = 20
    for row in myList: 
        for item in row:
            kurang -= item
    return kurang

print(getKurang([[10],[5]]))
print("================================\n")


## Notasi Big O get (O(logn))
print("================================")
def searchBinary(myList, item):
    first = 0
    last = len(myList)-1
    foundFlag = False
    while(first<=last and not foundFlag):
        mid = (first+last)//2 
        if myList[mid] == item : 
            foundFlag = True
        else:
            if item < myList[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return foundFlag
print(searchBinary([8,9,10,100,2000,300], 10))
print("================================\n")