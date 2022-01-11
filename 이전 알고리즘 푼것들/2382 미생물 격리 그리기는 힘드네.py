for tc in range(1, 1+int(input())):
    N, M, K = map(int, input().split())
    map_arr = [[0]*N for _ in range(N)]
    for _ in range(K):
        x, y, n, t = map(int, input().split())
        map_arr[x][y] = [n, t]

    for i in range(N):
        for j in range(N):
            if map_arr[i][j] != 0:
                if map_arr[i][j][1] == 1:
                    map_arr[i-1][j] = map_arr[i][j]
                    if i-1 == 0:
                        map_arr[i-1][j][1] = 2
                if map_arr[i][j][1] == 2:
                    map_arr[i + 1][j] = map_arr[i][j]
                    if i+1 == N:
                        map_arr[i-1][j][1] = 1
                if map_arr[i][j][1] == 3:
                    map_arr[i][j-1] = map_arr[i][j]
                    if j-1 == 0:
                        map_arr[i][j-1][1] = 4
                if map_arr[i][j][1] == 4:
                    map_arr[i][j+1] = map_arr[i][j]
                    if j+1 == N:
                        map_arr[i][j+1][1] = 3
                map_arr[i][j] = 0

    print(map_arr)