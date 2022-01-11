def dfs(start):
    INF = 0xffffff
    weight = [INF] * (V+1)
    weight[start] = 0

    group = [0] * (V+1)

    result = 0
    for _ in range(V+1):
        min_idx = 0
        min_v = INF
        for i in range(V+1):
            if weight[i] < min_v and group[i] == 0:
                min_idx = i
                min_v = weight[min_idx]
        group[min_idx] = 1
        result += weight[min_idx]

        for i in range(V+1):
            if weight[i] > arr[min_idx][i] and not group[i]:
                weight[i] = arr[min_idx][i]
    return result

for tc in range(1, 1+int(input())):
    V, E = map(int, input().split())
    INF = 0xffffff
    arr = [[INF]*(V+1) for _ in range(V+1)]

    for _ in range(E):
        n1, n2, w = map(int, input().split())
        arr[n1][n2] = w
        arr[n2][n1] = w

    result = dfs(0)

    print('#{} {}'.format(tc, result))