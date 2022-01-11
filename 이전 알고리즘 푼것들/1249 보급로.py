dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

def miro(x, y, num):
    global  min_num
    if x == N-1 and y == N-1:
        if min_num > num:
            min_num = num
        return

    if num > min_num:
        return

    for i in range(4):
        rx = x + dx[i]
        ry = y + dy[i]

        if 0 <= rx < N and 0 <= ry < N:
            if not visited[rx][ry]:
                if map_list[rx][ry] > num+arr[rx][ry]:
                    visited[rx][ry] = 1
                    map_list[rx][ry] = num + arr[rx][ry]
                    miro(rx, ry, num+arr[rx][ry])
                    visited[rx][ry] = 0

for tc in range(1, 1+int(input())):
    N = int(input())

    arr = [list(map(int, input())) for _ in range(N)]

    map_list = [[0xfffff]*N for _ in range(N)]

    visited = [[0]*N for _ in range(N)]

    min_num = 0xfffff

    map_list[0][0] = 0

    miro(0, 0, 0)

    print("#{} {}".format(tc, min_num))
