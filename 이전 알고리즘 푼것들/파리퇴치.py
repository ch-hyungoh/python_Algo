for tc in range(1, 1+int(input())):
    N, M = map(int,input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_num = 0
    for x in range(N-M+1):
        for y in range(N-M+1):
            num = 0
            for a in range(M):
                for b in range(M):
                    num += arr[x+a][y+b]

            if num > max_num:
                max_num = num

    print('#{} {}'.format(tc, max_num))