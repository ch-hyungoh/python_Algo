for tc in range(1, 1+int(input())):
    N = int(input())
    arr = list(input().split())
    result = []
    finish = []

    for i in range(len(arr)):
        flog = 1
        num = []
        for j in range(len(arr[i])):
            num.append(arr[i][j])
            if len(num) > 1:
                if num[j-1] > num[j]:
                    flog = 0
                    break
            if flog == 0:
                break
        if flog == 1:
            result.append(num)

    for i in range(len(result)):
        if len(result[i]) == 1:
            finish.append(int(result[i][0]))
        else:
            str = ''
            for j in range(len(result[i])):
                str += result[i][j]
            finish.append(int(str))

    max1 = 0
    max2 = 0

    if len(finish) < 2:
        re = -1
    else:
        for k in finish:
            if k > max1:
                max1 = k
        finish.remove(max1)

        for k in finish:
            if k > max2:
                max2 = k

        re = max1*max2

    print('#{} {}'.format(tc, re))