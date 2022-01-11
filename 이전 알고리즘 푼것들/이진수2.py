for tc in range(1, 1+int(input())):
    n = float(input())
    result = ''
    for i in range(1, 13):
        now = n // ((1/2)**i)
        result += str(int(now))
        n -= now * (1/2)**i
        if n == 0:
            break
    else:
        result = 'overflow'
    print('#{} {}'.format(tc, result))