from collections import deque

for tc in range(1, 1+int(input())):
    N = int(input())
    height = [list(map(int, input().split())) for _ in range(N)]
    cost = [[0xffffff] * N for _ in range(N)]

    q = deque()
    q.append((0, 0))
    cost[0][0] = 0

    while q:
        x,y = q.popleft()

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x+dx, y+dy
            if 0<= nx <N and 0<= ny < N:
                fuel = height[nx][ny] - height[x][y] +1 if height[nx][ny] - height[x][y] >0 else 1
                if cost[nx][ny] > cost[x][y] + fuel:
                    cost[nx][ny] = cost[x][y] + fuel
                    q.append((nx,ny))
    print('#{} {}'.format(tc, cost[-1][-1+
.






    ]))