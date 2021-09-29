# Hitung Konversi
print("Pertemuan DAA ke-5")
print("=====================================")
print("MENGHITUNG PERTUKARAN")
def countInversion(arr):
    result = 0
    for i in range (len(arr)):
        for j in range (i + 1, len(arr)):
            if arr[i]>arr[j]:
                result += 1
    return result

arr = [21, 70, 36, 14, 25]

result = countInversion(arr)
print(result)
print("=====================================\n")


print("=====================================")
print("MENGHITUNG INVERSI DENGAN DIVIDE ATAU CONQUER")
def countInversion2(arr):
    icount = 0
    if len(arr)<=1:
        return icount

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    icount += countInversion2(left)
    icount += countInversion2(right)
    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1 
            icount += (mid-i)
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(left):
        arr[k] = left[j]
        j += 1
        k += 1

    return icount

arr = [1, 20, 6, 4, 5] 
result2 = countInversion2(arr)
print(result2)    
print("=====================================\n")

print("=====================================")
print("MAXIMUM SUBARRAY SUM")
## TANPA DEVIDE DAN CONQUER
def maxSubSum(arr):
    max_so_far = 0
    max_ending_here = 0
    for i in range(len(arr)):
        max_ending_here += arr[i]
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

arr = [-2, -5, 6, -2, -3, 1, 5, -6]
result3 = maxSubSum(arr)
print(result3)
print("=====================================\n")

print("=====================================")
print("MAXIMUM SUBARRAY SUM DIVIDE")
## DENGAN DEVIDE DAN CONQUER
def maxCrossingSum(arr, low, mid, high):
    result4 = 0
    leftSum = float('-infinity')
    for i in range(mid, low-1, -1):
        result4 += arr[i]
        if result4 > leftSum:
            leftSum = result4
    result4 = 0
    rightSum = float('-infinity')
    for i in range(mid+1, high+1):
        result4 += arr[i]
        if result4 > rightSum:
            rightSum = result4
    return leftSum + rightSum

def maxSum(arr, low, high):
    if low == high:
        return arr[low]
    mid = (low + high)//2
    return max(maxSum(arr, low, mid), maxSum(arr, mid+1, high), maxCrossingSum(arr, low, mid, high))

arr = [-2, -5, 6, -2, -3, 1, 5, -6]
result4 = maxSum(arr, 0, len(arr)-1)
print(result4)
print("=====================================\n")


print("=====================================")
print("LONGEST COMMON PREFIX")
def commonPrefix(str1, str2):
    n1 = len(str1)
    n2 = len(str2)
    i,j = 0,0
    s = ""
    while i < n1 and j < n2:
        if str1[i] == str2[j]:
            s += str1[i]
            i += 1 
            j += 1
        else:
            break
    return s

def longestCommonPrefix(arr, low, high):
    if low == high:
        return arr[low]
    mid = (low + high)//2
    hasilCommon1 = longestCommonPrefix(arr, low, mid)
    hasilCommon2 = longestCommonPrefix(arr, mid+1, high)
    result5 = commonPrefix(hasilCommon1, hasilCommon2)
    return result5
    
arr = ['geeksforgeeks', 'geeks', 'geek', 'geezer']
arr2 = ['apple', 'aps', 'april']
result5 = longestCommonPrefix(arr, 0, len(arr)-1)
result6 = longestCommonPrefix(arr2, 0, len(arr2)-1)
print(result5)
print(result6)
print("=====================================\n")

print("=====================================")
print("MEDIAN 2 ARRAY URUT SAMA UKURAN")
def medianOfArray(arr1, arr2, n):
    m1 = -1
    m2 = -1
    count = 0
    i = j = 0
    while count < n+1:
        count += 1
        if i == n:
            m1 = m2
            m2 = arr2[0]
            break
        if j == n:
            m1 = m2
            m2 = arr1[0]
            break
        if arr1[i] < arr2[j]:
            m1 = m2
            m2 = arr1[i]
            i += 1
        else:
            m1 = m2
            m2 = arr2[j]
            j += 1
    return (m1+m2)//2
    
arr1 = [1, 12, 15, 26, 38]
arr2 = [2, 13, 17, 30, 45]
result7 = medianOfArray(arr1, arr2, len(arr1))
print(result7)
print("=====================================\n")

print("=====================================")
print("MEDIAN 2 ARRAY URUT BEDA UKURAN")
def floorSorted(arr, low, high, x):
    if low > high:
        return -1
    
    if arr[low] > x:
        return -1

    if arr[high] <= x:
        return arr[high]
    
    mid = (low + high)//2

    if arr[mid] == x:
        return arr[mid]

    if mid > 0 and x >= arr[mid-1] and arr[mid] > x:
        return arr[mid-1]

    if mid < high and x < arr[mid+1] and x >= arr[mid]:
        return arr[mid]

    if x > arr[mid]:
        return floorSorted(arr, mid+1, high, x)
    else:
        return floorSorted(arr, low, mid-1, x)

arr = [1, 2, 8, 10, 12, 14, 19]
x = 5
result8 = floorSorted(arr, 0, len(arr)-1, x)
print(result8)
print("=====================================\n")

print("=====================================")
print("NILAI TERDEKAT")
def closestNumber(arr, low, high, x):
    if low > high:
        return -1
    if arr[high] <= x:
        return arr[high]
    if arr[low] >= x:
        return arr[low]
    mid = (low + high)//2
    if arr[mid] == x:
        return arr[mid]
    abs_mid = abs(arr[mid]-x)
    if mid > 0:
        abs_left = abs(arr[mid-1]-x)
        if abs_left < abs_mid:
            return closestNumber(arr, low, mid-1, x)
    if mid < high:
        abs_right = abs(arr[mid+1]-x)
        if abs_right < abs_mid:
            return closestNumber(arr, mid+1, high, x)
    return arr[mid]

arr = [2, 5, 6, 7, 8, 8, 9]
x = 10
result9 = closestNumber(arr, 0, len(arr)-1, x)
print(result9)
print("=====================================\n")

print("=====================================")
print("FIXED POINT")
def fixedPoint(arr, low, high):
    if low > high:
        return -1
    if arr[high] == high:
        return arr[high]
    if arr[low] == low:
        return arr[low]
    mid = (low + high)//2
    if arr[mid] == mid:
        return arr[mid]
    if mid > arr[mid]:
        return fixedPoint(arr, mid+1, high)
    else: 
        return fixedPoint(arr, low, mid-1)

arr = [9, 0, 5, 3, 4]
result10 = fixedPoint(arr, 0, len(arr)-1)
print(result10)
print("=====================================\n")