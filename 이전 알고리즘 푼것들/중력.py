for tc in range(1, 1+int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    l = len(arr)
    max = 0
    for i in range(l):
        big = 0
        for j in range(i, l):
            if arr[i] <= arr[j]:
                big += 1
        result = N - i - big

        if result > max:
            max = result

    print('#{} {}'.format(tc, max))