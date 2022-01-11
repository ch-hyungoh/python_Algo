def solve(start):

    now_list = [now]*(V+1)
    now_list[start] = 1

    visit = [0]*(now+1)

    result = 0

    for _ in range(V+1):
        idx = 0
        vel = 0xfffff
        for i in range(V+1):
            if now_list[i] < vel and visit[i] == 0:
                idx = i
                vel = now_list[i]

        visit[idx] = 1
        result += now_list[idx]



for tc in range(1, 1+int(input())):
    now = 0xfffff
    N = int(input())
    V, E = map(int, input().split())

    arr = [[0xfffff]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        arr[n1][n2] = w

        