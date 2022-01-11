for tc in range(1, 1+int(input())):
    N, K = map(int,input().split())

    arr = [(list(map(int,input().split()))+[0]) for _ in range(N)]
    arr.append([0]*(N+2))
    result = 0

    for a in range(N+1):
        b = 0
        while b <= N:
            count = 0
            if arr[a][b] == 1:
                while arr[a][b] > 0:
                    count += 1
                    b += 1
                if count == K:
                    result += 1
            b += 1

    for b in range(N+2):
        a = 0
        while a <= N:
            count = 0
            if arr[a][b] == 1:
                while arr[a][b] > 0:
                    count += 1
                    a += 1
                if count == K:
                    result += 1
            a += 1
    print('#{} {}'.format(tc, result))