def solve(idx, cnt, remain):
    global min_num
    if idx == N-1:
        if cnt < min_num:
            min_num = cnt
    # 배터리를 충전하냐
    # 배터리 남아있는 경우 안하냐

    # 배터리 교환하는 경우
    solve(idx+1, cnt+1, stops[idx]-1)
    # 배터리 교환안하는 경우
    if remain > 0:
        solve(idx+1, cnt, remain-1)


# 멱집합(powerset)
for tc in range(1, 1+int(input())):
    arr= list(map(int,input().split()))
    N = arr[0]
    stops = arr[1:]
    min_num = 798456123
    solve(1, 0, stops[0])

    print(min_num)