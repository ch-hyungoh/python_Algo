for tc in range(1, 1+int(input())):
    N, M = map(int,input().split())
    arr = list(map(int, input().split()))
    min = 789456132456
    max = 0
    for i in range(N-M+1):
        sum = 0
        for j in range(M):
            sum += arr[i+j]
        if sum > max:
            max = sum
        if sum < min:
            min = sum

    print('#{} {}'.format(tc, (max-min)))