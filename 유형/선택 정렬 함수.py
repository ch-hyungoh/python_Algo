def selectionsort(start, end):
    if arr[start] > arr[end]:
        arr[start], arr[end] = arr[end], arr[start]
    mid = end//2
    selectionsort(start, mid)
    selectionsort(mid, end)

arr = [1,2,3,4,5]

