dr = [0, 1]
dc = [1, 0]
for tc in range(1, 1+int(input())):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    col = [0] * 21
    sel = [0] * 21
    count_list = []

    for i in range(N):
        for j in range(N):
            count = 0
            if arr[i][j] != 0:
                for k in range(2):
                    for l in range(N):
                        nr = i + (dr[k]*l)
                        nc = j + (dc[k]*l)
                        if nr >= N or nc >= N:

                            if arr[i][j]