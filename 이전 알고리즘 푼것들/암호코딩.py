pwd = {
    (3, 2, 1, 1): 0,
    (2, 2, 2, 1): 1,
    (2, 1, 2, 2): 2,
    (1, 4, 1, 1): 3,
    (1, 1, 3, 2): 4,
    (1, 2, 3, 1): 5,
    (1, 1, 1, 4): 6,
    (1, 3, 1, 2): 7,
    (1, 2, 1, 3): 8,
    (3, 1, 1, 2): 9
}

# 암호코드의 첫번째 줄의 시작위치 또는 끝위치
def check_code():
    for i in range(N):
        for j in range(M - 1, 0, -1):
            if arr[i][j] == '0': continue
            # 암호코드의 마지막 열 위치 j, 시작 = j - 55
            # 8개의 암호패턴을 읽어서 숫자로 변환
            read = []
            idx = j
            for _ in range(8):
                # 0 1 0 1 의 개수를 카운팅한다.
                c1 = c2 = c3 = c4 = 0
                while arr[i][j] == '1':
                    c4 += 1
                    idx -= 1
                while arr[i][j] == '0':
                    c3 += 1
                    idx -= 1
                while arr[i][j] == '1':
                    c2 += 1
                    idx -= 1
                c1 = 7-(c2+c3+c4)
                idx -= c1

            odd = read[0] + read[2] + read[4] + read[6]
            even = read[1] + read[3] + read[5] + read[7]

            if (odd * 3 + even) % 10 == 0:
                return odd + even
            else:
                return 0

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    print('#{} {}'.format(tc, check_code()))