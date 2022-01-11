# import sys
# sys.stdin = open('1234_input.txt')
codes = {
    (3,2,1,1) : 0,
    (2,2,2,1) : 1,
    (2,1,2,2) : 2,
    (1,4,1,1) : 3,
    (1,1,3,2) : 4,
    (1,2,3,1) : 5,
    (1,1,1,4) : 6,
    (1,3,1,2) : 7,
    (1,2,1,3) : 8,
    (3,1,1,2) : 9
}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    password = list()  # 암호코드 저장
    result = False  # 출력할 값은, 코드 비정상이면 False를 준다.
    for i in range(N): # i는 행의 번호
        # 뒤에서 부터 읽으면서 암호코드 찾기
        idx = M-1 # 맨뒤에서 부터 시작

        w1 = w2 = w3 = w4 = 0  # 각 코드들의 너비를 저장할 변수들
        while arr[i][idx] == 1:
            w4 += 1
            idx -= 1
        while arr[i][idx] == 0:
            w3 += 1
            idx -= 1
        while arr[i][idx] == 1:
            w2 += 1
            idx -= 1
        min_num = min(w2, w3, w4)
        w1 = 7 - (w2/min_num + w3/min_num + w4/min_num)
        w1 = w1*min_num
        password.insert(0, codes[(w1, w2, w3, w4)])
        idx -= w1

        odd_sum = password[0] + password[2] + password[4] + password[6]
        # 짝수자리 합( 인덱스는 홀수)
        even_sum = password[1] + password[3] + password[5] + password[7]
        check_sum = odd_sum * 3 + even_sum
        if check_sum % 10 == 0:  # 10의 배수
            result = odd_sum + even_sum


