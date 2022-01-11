
# r, c : bfs 시작점
def solve(r, c):
    queue = list()
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    result = 1
    queue.append((r, c, result))
    while queue:
        cc, cr, result = queue.pop(0)
        for d in range(4):
            nr = cr + dr[d]
            nc = cc + dc[d]
            if 0<= nc < N and 0 <= N:
                if rooms[nr][nc] - rooms[cr][cc] == 1:
                    queue.append((nc,nr,result+1))
    return (rooms[r][c], result)
for tc in range(1, 1+int(input())):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    min_num = N*N+1
    max_lenth = 0
    for i in range(N):
        for j in range(N):
            rn, result = solve(i, j)
            if result >= max_lenth:
                pass
            elif result == max_lenth:
                if min_num > rn:
                    min_num = rn
    print('#{} {}'.format(tc, max_lenth))