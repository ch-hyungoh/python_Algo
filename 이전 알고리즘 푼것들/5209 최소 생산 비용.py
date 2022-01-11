def solve(num):
    global number
    global min
    if number > min:
        return
    if num == N:
        if min > number:
            min = number
    for a in range(N):
        if not visit[a]:
            number += arr[a][num]
            visit[a] = 1
            solve(num+1)
            number -= arr[a][num]
            visit[a] = 0

for tc in range(1, 1+int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min = 789456123
    number = 0
    visit = [0]*N

    solve(0)
    print("#{} {}".format(tc, min))
