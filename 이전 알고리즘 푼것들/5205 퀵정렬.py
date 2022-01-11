def sort(arr, start, end):
    pivot = arr[start]
    i = start
    j = end
    while i <= j:
        while i < len(arr) and arr[i] <= pivot:
            i += 1
        while j >= 0 and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[start], arr[j] = arr[j], arr[start]
    return j

def quik(arr, start, end):
    if start >= end:
        return
    pivot_idx = sort(arr, start, end)
    quik(arr, start, pivot_idx - 1)
    quik(arr, pivot_idx + 1, end)


for tc in range(1, 1+int(input())):
    N = int(input())
    arr= list(map(int, input().split()))
    quik(arr, 0, N-1)

    print("#{} {}".format(tc, arr[N//2]))

