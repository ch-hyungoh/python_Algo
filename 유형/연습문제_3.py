# 0269FAC9A0
def hex_to_decimal(c):
    #16진수를 받았을 때,
    #해당숫자의 아스키 코드를 알아내고
    #ord() 아스키코드 얻어오기
    # 모양이 숫자일때 >> ord('숫자') - ord('0')
    # 모양이 숫자일때 >> ord('알파벳') - ord('A') + 10
    """
    :param c: 16진수를 나타내는 문자하나
    :return: c 의 2진수 문자열
    """
    # 아스키코드 얻어오기
    num = ord(c)
    if '0' <= c <= '9':
        return num - ord('0')
    else:
        return num - ord('A') + 10

# 10진수 > 2진수
def decimal_to_binary(n):
    #n : 10 진수
    # 10진수를 2진수로 만들기
    binary = [0] * 4
    idx = 3
    while n > 0:
        binary[idx] = n % 2
        idx -= 1
        n //= 2
    return binary

data = input()
result = []
for i in range(len(data)):
    result += decimal_to_binary(hex_to_decimal(data[i]))

# 주어진 2진 문자열에서 암호 코드 찾아서 출력하기
print(result)

patterns = {
    '001101' : 0,
    '010011' : 1,
    '111011' : 2,
    '110001' : 3,
    '100011' : 4,
    '110111' : 5,
    '001011' : 6,
    '111101' : 7,
    '011001' : 8,
    '101111' : 9,
}



# 뒤에서 부터 읽어오기
i = len(result) - 1
while i > -1:
    # 만약에 result[i] == 1이라면 암호패턴의 시작
    if result[i] == 1: # 암호패턴 시작
        # 6개 읽어오기
        pattern = []
        for j in range(i,i-6,-1):
            pattern.insert(0,str(result[j]))
        i -= 6
        print(patterns[''.join(pattern)],end=' ')
    else:
        #그냥 지나가면 됩니다.
        i -= 1




