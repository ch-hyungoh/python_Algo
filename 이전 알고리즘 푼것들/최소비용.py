dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]
def solve(x, y, sums):
    global sum_min
    # 루트 전부다 체크해서 x , y == N이 되는 부분 찾기 이 되는 부분에서
    # sums 가 최소가 되는 최솟값 찾기
    if x == (N-1) and y == (N-1):
        if sum_min > sums:
            sum_min = sums
    if sums > sum_min:
        return
    for i in range(4):
        nx = x+dr[i]
        ny = y+dc[i]
        if 0<= nx < N and 0<= ny < N:
            if not visited[nx][ny]:
                visited[nx][ny] = 1
                solve(nx, ny, sums+(arr[nx][ny]-arr[x][y]+1))
                visited[nx][ny] = 0

for tc in range(1, 1+int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    sum_min = 0xffffff

    visited[0][0] = 1
    solve(0, 0, 0)

    print('#{} {}'.format(tc, sum_min))

