N = int(input())

map_list = []

for i in range(N):
    x, y = map(int,input().split())
    map_list.append([x,y,1])

k = 0

while k < N:
    count = 1
    for a in range(N):
        if (map_list[a][0] > map_list[k][0]) and (map_list[a][1] > map_list[k][1]):
            count += 1

    map_list[k][2] = count
    k += 1

for i in range(N):
    if i == (N-1):
        print(map_list[i][2])
    else:
        print(map_list[i][2], end=' ')