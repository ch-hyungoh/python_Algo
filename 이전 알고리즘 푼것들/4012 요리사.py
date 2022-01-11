def combination(arr, num):
    if num == N//2:
        print()
    else:


def solve():
    global taste_min
    if len(result) == N:
        k, j = 0, 0
        for i in range(N):
            if i < N/2:
                k += result[i]
            else:
                j += result[i]
        abss = abs(k-j)
        if abss < taste_min:
            taste_min = abss
    for a in range(N):
        for b in range(N):
            if b != a and not menu[a] and not menu[b]:
                menu[a] = 1
                menu[b] = 1
                result.append(arr[a][b])
                result.append(arr[b][a])
                solve()
                menu[a] = 0
                menu[b] = 0
                result.pop()
                result.pop()

for tc in range(1, 1+int(input())):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    com = []
    for i in range(N):
        com.append(i)
    sel = [0] * (N//2)
    check = [0] * N
    combi = []
    taste_min = 789456
    menu = [0]*N

    result = []

    solve()

    print('#{} {}'.format(tc, taste_min))