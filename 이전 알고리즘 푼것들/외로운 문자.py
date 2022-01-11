for tc in range(1, 1+int(input())):
    arr = list(input())

    str_list = []
    result = ''

    for i in arr:
        if i in str_list:
            str_list.pop(str_list.index(i))
        else:
            str_list.append(i)

    str_list.sort()

    if str_list:
        for i in str_list:
            result += i
    else:
        result = 'Good'

    print('#{} {}'.format(tc, result))