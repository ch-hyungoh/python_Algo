for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    # 1 : N극 2 : S극 위 : N극 아래 : S극
    # 1. 바닥으로 떨어질것들 찾기
    # 2. 같은줄에 한개라도 다른극이 있으면 안떨어짐

    num = 0
    for i in range(100):
        for j in range(100):
            if arr[i][j] == 1 and i+1 < N:
                if arr[i+1][j] == 0 or arr[i+1][j] == 1:
                    arr[i+1][j] = 1
                elif arr[i+1][j] == 2:
                    arr[i][j] = 1
            if arr[i][j] == 2 and i > 0:
                if arr[i-1][j] == 0 or arr[i-1][j] == 2:
                    arr[i-1][j] = 2
                elif arr[i-1][j] == 1:
                    arr[i][j] = 2

    for i in range(100):
        for j in range(100):
            if arr[i][j] == 1 and i+1 < N:
                if arr[i+1][j] == 2:
                    num += 1

    print('#{} {}'.format(tc, num))