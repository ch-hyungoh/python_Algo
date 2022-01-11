def dfs(start):
    weight = arr[start][:]
    U = {start}

    while len(U) < V+1:
        min_v = 0xfffffff
        min_idx = -1
        for i in range(V+1):
            if i not in U and min_v > weight[i]:
                min_v = weight[i]
                min_idx = i
        U.add(min_idx)

        for i in range(V+1):
            if i not in U and arr[min_idx][i] + weight[min_idx] < weight[i]:
                weight[i] = arr[min_idx][i] + weight[min_idx]
    return weight[V]

for tc in range(1, 1+int(input())):
    V, E = map(int, input().split())
    arr = [[0xfffff]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        arr[n1][n2] = w

    result = dfs(0)

    print('#{} {}'.format(tc, result))