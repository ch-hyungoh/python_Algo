def change(number):
    patterns_num = {
        '1101000': 9,
        '1110110': 8,
        '1101110': 7,
        '1111010': 6,
        '1000110': 5,
        '1100010': 4,
        '1011110': 3,
        '1100100': 2,
        '1001100': 1,
        '1011000': 0
    }
    return patterns_num[number]

for test in range(1, 1+int(input())):
    n,m = map(int,input().split())

    arr = []
    patterns = []
    solve = []
    code_num = []

    start = False
    result = False


    for i in range(n):
        arr.append(list(input()))

    for j in range(n-1, -1, -1):
        for k in range(m-1,- 1, -1):
            if arr[j][k] == '1':
                start = True
            if start == True and result == False:
                solve.append(arr[j][k])
            if len(solve) == 56:
                result = True


    i = 56-1
    while i >-1:
        pattern = []
        for j in range(i,i-7,-1):
            pattern.insert(0, solve[j])
        i -= 7
        patterns.append(change(''.join(pattern)))

    result = (patterns[0]+patterns[2]+patterns[4]+patterns[6])*3 + patterns[1] + patterns[3] + patterns[5]+ patterns[7]
    if result % 10 == 0:
        result = sum(patterns)
        print("#{} {}".format(test, result))
    else:
        print("#{} 0".format(test))
