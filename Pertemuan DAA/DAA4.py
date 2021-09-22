## MENUKAR VARIABLE
print("Pertemuan DAA ke-4")
print("=====================================")
print("MENUKAR VARIABLE")
var1 = 1
var2 = 2 
var3 = 3
var1, var2, var3 = var3, var2, var1
print(var1, var2, var3)
print("=====================================\n")

## BUBBLE SORTING LOOP DALAM
print("=====================================")
print("BUBBLE SORTING LOOP DALAM")
list = [25, 21, 22, 24, 23, 27, 26]
lastElementIndex = len(list) -1
print(0, list)
for idx in range(lastElementIndex):
    if list[idx]>list[idx+1]:
        list[idx], list[idx+1] = list[idx+1], list[idx]
    print(idx+1, list)
print("=====================================\n")

## BUBBLE SORTING LOOP LUAR
print("=====================================")
print("BUBBLE SORTING LOOP LUAR")
list = [21, 22, 24, 23, 25, 26, 27]
def BubbleSort(list):
    lastElementIndex = len(list)-1
    for passNo in range(lastElementIndex, 0, -1):
        for idx in range(passNo):
            if list[idx]>list[idx+1]:
                list[idx], list[idx+1] = list[idx+1], list[idx]
    return list

list2 = [28, 30, 21, 40, 25, 27, 36]
print(BubbleSort(list2))
print(list2)
print("=====================================\n")

## LATIHAN BUBBLE SORT
print("=====================================")
print("LATIHAN BUBBLE SORT")
list = [100, 20, 60, 90, 40, 30, 10]
def BubbleSort(list):
    lastElementIndex = len(list)-1
    for passNo in range(lastElementIndex, 0, -1):
        for idx in range(passNo):
            if list[idx]>list[idx+1]:
                list[idx], list[idx+1] = list[idx+1], list[idx]
    return list

print(BubbleSort(list))
print("=====================================\n")

## INSERTION SORT
print("=====================================")
print("INSERTION SORT")
list = [35, 31, 32, 34, 33, 37, 36]
def InsertionSort(list):
    for i in range(1, len(list)):
        j = i-1
        next = list[i]

        while(list[j] > next) and (j >= 0):
            list[j+1] = list[j]
            j = j-1
            list[j+1] = next
    return list

print(InsertionSort(list))
print("=====================================\n")

## LATIHAN INSERTION SORT
print("=====================================")
print("LATIHAN INSERTION SORT")
list = [89, 12, 57, 16, 25, 11, 75]
def InsertionSort(list):
    for i in range(1, len(list)):
        j = i-1
        next = list[i]

        while(list[j] > next) and (j >= 0):
            list[j+1] = list[j]
            j = j-1
            list[j+1] = next
    return list

print(InsertionSort(list))
print("=====================================\n")

## SELECTION SORT
print("=====================================")
print("SELECTION SORT")
list = [89, 12, 57, 16, 25, 11, 75]
def SelectionSort(list):
    for fill_slot in range(len(list) - 1, 0, -1):
        max_index = 0
        for location in range(1, fill_slot + 1):
            if list[location] > list[max_index]:
                max_index = location
        list[fill_slot], list[max_index] = list[max_index], list[fill_slot]
    return list

print(SelectionSort(list))
print("=====================================\n")

## LATIHAN SELECTION SORT
print("=====================================")
print("LATIHAN SELECTION SORT")
list = [89, 12, 57, 16, 25]
def SelectionSort(list):
    for fill_slot in range(len(list) - 1, 0, -1):
        max_index = 0
        for location in range(1, fill_slot + 1):
            if list[location] > list[max_index]:
                max_index = location
        list[fill_slot], list[max_index] = list[max_index], list[fill_slot]
    return list

print(SelectionSort(list))
print("=====================================\n")

## LINEAR SEARCH
print("=====================================")
print("LINEAR SEARCH")
list = [89, 12, 57, 16, 25, 20, 50]
def LinearSearch(list, item):
    index = 0
    found = False

    while index < len(list) and found is False:
        if list[index] == item:
            found = True
            print("Angka " + str(item) + " ada di List")
        else:
            index = index + 1
    return found

print(LinearSearch(list, 12))
print(LinearSearch(list, 31))
print("=====================================\n")

## LATIHAN LINEAR SEARCH
print("=====================================")
print("LATIHAN LINEAR SEARCH")
list = ["y", "u", "i", "w", "o", "a", "q", "u", "j", "p"]
def LinearSearch(list, item):
    index = 0
    found = False

    while index < len(list) and found is False:
        if list[index] == item:
            found = True
            print("Huruf (" + str(item) + ") ada di List")
        else:
            index = index + 1
    return found

print(LinearSearch(list, 'a'))
print("=====================================\n")

## BINARY SEARCH
print("=====================================")
print("BINARY SEARCH")
list = [12, 33, 11, 99, 22, 55, 90]
def BinarySearch(list, item):
    first = 0
    last = len(list)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if list[midpoint] == item:
            found = True
        else:
            if item < list[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

sorted_list = BubbleSort(list)
print(BinarySearch(list, 12))
print(BinarySearch(list, 91))
print("=====================================\n")

## LATIHAN BINARY SEARCH
print("=====================================")
print("LATIHAN BINARY SEARCH")
list = ["y", "u", "i", "w", "o", "a", "q", "u", "j", "p"]
def BinarySearch(list, item):
    first = 0
    last = len(list)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if list[midpoint] == item:
            found = True
            print("Huruf (" + str(item) + ") ada di List")
        else:
            if item < list[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found

sorted_list = BubbleSort(list)
print(BinarySearch(list, "a"))
print("=====================================\n")

## INTERPOLATION SEARCH
print("=====================================")
print("INTERPOLATION SEARCH")
list = [12, 33, 11, 99, 22, 55, 90]
def InterpolationSearch(list, x):
    idx0 = 0
    idxn = (len(list)-1)
    found = False

    while idx0 <= idxn and x >= list[idx0] and x <= list[idxn]:
        mid = idx0 + int(((float(idxn - idx0) / (list[idxn] - list[idx0])) * (x - list[idx0])))
        if list[mid] == x:
            found = True
            return found
        
        if list[mid] < x:
            idx0 = mid + 1
    return found

sorted_list = BubbleSort(list)
print(InterpolationSearch(list, 12))
print(InterpolationSearch(list, 91))
print("=====================================\n")

## LATIHAN INTERPOLATION SEARCH
print("=====================================")
print("LATIHAN INTERPOLATION SEARCH")
list = [2020071048, 2020071041]
def InterpolationSearch(list, x):
    idx0 = 0
    idxn = (len(list)-1)
    found = False

    while idx0 <= idxn and x >= list[idx0] and x <= list[idxn]:
        mid = idx0 + int(((float(idxn - idx0) / (list[idxn] - list[idx0])) * (x - list[idx0])))
        if list[mid] == x:
            found = True
            print("NIM (" + str(x) + ") Adalah Aldho Sukadi")
            return found
        
        if list[mid] < x:
            idx0 = mid + 1
    return found

sorted_list = BubbleSort(list)
print(InterpolationSearch(list, 2020071048))
print("=====================================\n")

## LATIHAN INTERPOLATION SEARCH MENGGUNAKAN HURUF MASIH BELUM BISA
print("=====================================")
print("LATIHAN INTERPOLATION SEARCH MENGGUNAKAN HURUF MASIH BELUM BISA")
list = ["y", "u", "i", "w", "o", "a", "q", "j", "p"]
def InterpolationSearch(list, x):
    idx0 = 0
    idxn = (len(list)-1)
    found = False

    while idx0 <= idxn and x >= list[idx0] and x <= list[idxn]:
        mid = idx0 + int(((float(idxn - idx0) / (list[idxn] - list[idx0])) * (x - list[idx0])))
        if list[mid] == x:
            found = True
            print("Huruf (" + str(x) + ") ada di List")
            return found
        
        if list[mid] < x:
            idx0 = mid + 1
    return found

print(InterpolationSearch(str(list), "y"))
print("=====================================\n")
