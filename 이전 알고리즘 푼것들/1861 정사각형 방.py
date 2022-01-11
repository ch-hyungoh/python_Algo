rx = [0, 1, 0, -1]
ry = [1, 0, -1, 0]

def solve(x, y, num):
    global max
    for i in range(4):
        nx = x + rx[i]
        ny = y + ry[i]
        if 0 <= nx <N and 0<= ny <=N and (arr[x][y]+1 == arr[nx][ny]):
            solve(nx, ny, num+1)
    else:
        if num >= max:
            max = num
            return
for tc in range(1, 1+int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max = 0

    solve(0, 0, 0)