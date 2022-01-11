def solve(num):
    global number
    global max
    if (number*100) < (max*100):
        return
    if num == N:
        if max < number:
            max = number
    for a in range(N):
        if not visit[a] and (arr[a][num] != 0):
            number *= arr[a][num]
            visit[a] = 1
            solve(num+1)
            number /= arr[a][num]
            visit[a] = 0

for tc in range(1, 1+int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for a in range(N):
        for b in range(N):
            arr[a][b] = (arr[a][b]/100)
    max = 0
    number = 1
    visit = [0]*N

    solve(0)
    print("#{} {:.6f}".format(tc, (max*100)))
