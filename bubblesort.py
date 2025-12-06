def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [12,4,14,12,4,63,23,7,7,2,7,0]
arr = bubble_sort(arr)
print("Sorted array: ", arr)
