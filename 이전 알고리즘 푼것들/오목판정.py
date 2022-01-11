for tc in range(1, 1+int(input())):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 'o':
                cnt += 1
            if cnt == 5:
                result = 1
                break
            elif arr[i][j] == '.':
                cnt = 0

    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 'o':
                cnt += 1
            if cnt == 5:
                result = 1
                break
            elif arr[j][i] == '.':
                cnt = 0

    for i in range(N-4):
        for j in range(N-4):
            cnt = 0
            for a in range(5):
                if arr[i+a][j+a] == 'o':
                    cnt += 1
                if cnt == 5:
                    result = 1
                    break
                elif arr[i+a][j+a] == '.':
                    cnt = 0

    for i in range(N-4):
        for j in range(N - 4):
            cnt = 0
            for a in range(5):
                if arr[i+a][N-j-a-1] == 'o':
                    cnt += 1
                if cnt == 5:
                    result = 1
                    break
                elif arr[i+a][N-j-a-1] == '.':
                    cnt = 0

    if result:
        print('#{} YES'.format(tc))
    else:
        print('#{} NO'.format(tc))