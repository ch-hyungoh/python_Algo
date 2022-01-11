for tc in range(1, 1+int(input())):
    N, M, K = map(int, input().split())
    num_list = []
    N = N-1
    for _ in range(K):
        x, y, n, t = map(int, input().split())
        num_list.append([x, y, n, t])
    for _ in range(M):
        for i in num_list:
            if i[3] == 1:
                i[0] -= 1
                if i[0] == 0:
                    i[3] = 2
                    i[2] //= 2
            elif i[3] == 2:
                i[0] += 1
                if i[0] == N:
                    i[3] = 1
                    i[2] //= 2
            elif i[3] == 3:
                i[1] -= 1
                if i[1] == 0:
                    i[3] = 4
                    i[2] //= 2
            elif i[3] == 4:
                i[1] += 1
                if i[1] == N:
                    i[3] = 3
                    i[2] //= 2

        for i in range(len(num_list)-1):
            for k in range(i+1, len(num_list)):
                if (num_list[i][0] == num_list[k][0]) and (num_list[i][1] == num_list[k][1]):
                    if num_list[i][2] > num_list[k][2]:
                        num_list[k][3] = num_list[i][3]
                        # print(i, k)
                    else:
                        num_list[i][3] = num_list[k][3]
                        # print(i, k)
        # print(num_list)

        for i in range(len(num_list) - 1):
            for k in range(i + 1, len(num_list)):
                if (num_list[i][0] == num_list[k][0]) and (num_list[i][1] == num_list[k][1]):
                    num_list[i][2] += num_list[k][2]
                    num_list[k][2] = 0

    sum = 0
    for i in num_list:
        sum += i[2]
    print('#{} {}'.format(tc, sum))