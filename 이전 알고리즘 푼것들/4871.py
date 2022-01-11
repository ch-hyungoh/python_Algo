for test in range(1, 1+int(input())):
    v, e = map(int,input().split())

    maps = [[0]*(v+1) for _ in range(v+1)]

    for i in range(e):
        s, g = map(int,input().split())
        maps[s][g] = 1

    start, end = map(int,input().split())

    stack = [start]
    visited = [0]*(v+1)
    result = False

    while stack:
        now = stack[-1]
        visited[now] = 1
        if now == end:
            result = True
            break
        for k in range(v+1):
            if not visited[k] and maps[now][k]:
                visited[k] = 1
                stack.append(k)
                break
        else:
            stack.pop()

    if result:
        print("#{} 1".format(test))
    else:
        print("#{} 0".format(test))