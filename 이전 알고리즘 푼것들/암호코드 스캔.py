codes = {
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
ha_dok = {

}
# 암호코드를 검사하는 함수
def solve(arr):
    #행우선 순회
    # 열 순회할때는 뒤에서 부터...
    result = 0
    for i in range(N):
        #j 인덱스는 뒤에서 부터 M*4-1(16진수가 4비트 2진수로 변경되면서 길이가 4배 늘어남)
        j = M*4-1
        password = []
        while j>= 55:
            if arr[i][j] == 1 and arr[i-1][j] == 0: # 암호코드의 시작이다( 뒤에서 부터)
                #암호코드 해석
                for _ in range(8):
                    # 코드를 읽고 숫자 하나 찾기
                    # 4번째 1 길이 읽기
                    w1 = w2 = w3 =w4 = 0
                    while arr[i][j] == 1:
                        w4 += 1
                        j -= 1
                    # 3번째 1 길이 읽기
                    while arr[i][j] == 0:
                        w3 += 1
                        j -= 1
                    # 2번째 1 길이 읽기
                    while arr[i][j] == 1:
                        w2 += 1
                        j -= 1
                    #암호코드 뒤 세자리의 길이에는 1이 최소한 하나는 포함
                    # 그중에서 가장 작은 값을 뽑아내면, 암호코드가 늘어나는 배울
                    rate = min(w2, w3, w4)
                    w2 //= rate
                    w3 //= rate
                    w4 //= rate
                    w1 = 7 - w2 - w3 - w4
                    j -= w1 * rate
                password.append(codes[(w1, w2, w3, w4)]) #암호코드가 나타내는 숫자 하나
            password.reverse() # 뒤에서 부터 암호를 읽어서 뒤집어져 있으므로
                    #암호가 8개 만들어 졌으므로 정상적인 코드인지 확인하기
            odd_sum = password[0] + password[2] + password[4] + password[6]
            even_sum = password[1] + password[3] + password[5] + password[7]
            if(odd_sum*3 + even_sum)% 10 == 0: # 정상적인 암호일때 누적합 구하기
                result += odd_sum + even_sum
            else:
                j -= 1 #암호코드는 아직 시작아지 않았으므로 다음칸 검사

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    arr = [] #2차원 배열 주소 저장

    for i in range(N): #세로길이
        tmp = [] # 행 저장 배열-
        for j in range(M): #가로길이
            tmp += codes[data[i][j]]
        # 2진수 행 하나 완성
        arr.append(tmp) #행을 2차원 배열에 추가
    result = solve(arr)


    print("#{} {}".format(tc, result))