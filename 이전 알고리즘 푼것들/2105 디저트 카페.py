# 디저트 카페
# 대각선으로만 움직이며 원래 출발한 카페로 돌아와야한다.
# 같은 종류 없애기 eated :
# 마름모 이므로 각각의 길이가 2개 같아야 한다
dr = (1, 1, -1, -1)
dc = (1, -1, -1, 1)

def dfs(r, c, num):
    global start, max_val
    if num == 3 and (r, c) == start:
        val = 0
        for eat in eated:
            if eat:
                val += 1
        if val > max_val:
            max_val = val

    if r < 0 or r >= N or c < 0 or c >= N or eated[arr[r][c]]:
        return

    eated[arr[r][c]] = 1

    nr1, nc1 = r + dr[num], c + dc[num]
    dfs(nr1, nc1, num)

    if num != 3:
        nr2, nc2 = r + dr[num+1], c + dc[num+1]
        dfs(nr2, nc2, num+1)

    eated[arr[r][c]] = 0



for tc in range(1, 1+int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_val = -1
    eated = [0]*101

    for i in range(N - 1):
        for j in range(1, N - 1):
            start = (i, j)
            dfs(i, j, 0)

    print('#{} {}'.format(tc, max_val))

