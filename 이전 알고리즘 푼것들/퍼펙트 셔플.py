for tc in range(1, 1+int(input())):
    N = int(input())
    str_list = list(input().split())

    odd_list = []
    mid_list = []
    k = (N // 2)

    print('#{}'.format(tc), end=' ')
    for i in range(N):
        if i < k:
            odd_list.append(str_list[i])
        else:
            mid_list.append(str_list[i])

    if N % 2 == 0:
        while odd_list or mid_list:
            fir, sec = odd_list.pop(0), mid_list.pop(0)
            print('{} {}'.format(fir, sec), end=' ')
            if len(odd_list) == 1:
                fir, sec = odd_list.pop(0), mid_list.pop(0)
                print('{} {}'.format(fir, sec))
    else:
        while odd_list or mid_list:
            if len(mid_list) == 1:
                sec = mid_list.pop(0)
                print('{}'.format(sec))
                break
            fir, sec = odd_list.pop(0), mid_list.pop(1)
            print('{} {}'.format(fir, sec), end=' ')
