def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(x)

def union(x,y):
    a = find_set(x)
    b = find_set(y)
    if a == b:
        return
    else:
        p[b] = a

for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())

    arr = list(map(int, input().split()))

    groups = [0]*(N+1)

