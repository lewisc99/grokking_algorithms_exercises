def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i 
    return smallest_index

def selectionSort(arr):
    newArr = []
    copiedArr = list(arr)
    for i in range(len(copiedArr)):
        smallest = findSmallest(copiedArr)
        newArr.append(copiedArr.pop(smallest))
    return newArr

print(selectionSort([5, 3, 6, 2, 10])) # [2, 3, 5, 6, 10]
print(selectionSort([4,1,81,20])) # [1, 4, 20, 81]
