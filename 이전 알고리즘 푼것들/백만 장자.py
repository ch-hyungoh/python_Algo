for tc in range(1, 1+int(input())):
    N = int(input())

    arr = list(map(int, input().split()))
    num = N-1
    now = 1
    result = 0
    while num > 0:
        while arr[num] > arr[num-now]:
            result += arr[num] - arr[num-now]
            now += 1
            if num-now < 0:
                break
        num -= now
        now = 1

    print('#{} {}'.format(tc, result))

    # 1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
    # 2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
    # 3. 판매는 얼마든지 할 수 있다.