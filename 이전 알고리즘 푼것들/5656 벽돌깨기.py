dr = [-1, 0, 0]
dc = [0, 1, -1]
def breaken(a, b, num):
    for a in range(num - 1):
        for b in range(3):
            ir = a + dr[b]
            jc = b + dc[b]
            arr[ir][jc] = 0


def solve(num):
    for i in range(W):
        for j in range(H):
            if arr[i][j] != 0 and arr[i][j-1] == 0:
                now = arr[i][j]
                arr[i][j] = 0
                breaken(i, j, now)
                solve(num+1)


for tc in range(1, 1+int(input())):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    print(arr)
    min_num = H*W+1
    solve(0)
    print(arr)