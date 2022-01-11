for tc in range(1, 1+int(input())):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    ans = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for i in range(9):
        stock = [0] * 10
        for j in range(9):
            stock[arr[i][j]] += 1
        for k in range(10):
            if stock[k] == 2:
                result = 0
                break

    for j in range(9):
        stock = [0] * 10
        for i in range(9):
            stock[arr[i][j]] += 1
        for k in range(10):
            if stock[k] >= 2:
                result = 0
                break

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            stock = [0] * 10
            for a in range(3):
                for b in range(3):
                    stock[arr[i+a][j+b]] += 1
            for k in range(10):
                if stock[k] >= 2:
                    result = 0
                    break


    if result:
        print('#{} 1'.format(tc))
    else:
        print('#{} 0'.format(tc))
