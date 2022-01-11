for tc in range(1, 1+int(input())):
    N, K = map(int, input().split())
    num_list = list(input())

    N_big = N//4
    N_list = []

    for number in range(N_big):

        for i in range(0, N, N_big):
            N_now = ''
            for k in range(N_big):
                N_now += num_list[i+k]
            N_list.append(N_now)

        k = num_list.pop(-1)
        num_list.insert(0, k)

    final_list = []
    for i in N_list:
        number = ''
        for j in i:
            if j == '0':
                number += '0000'
            if j == '1':
                number += '0001'
            if j == '2':
                number += '0010'
            if j == '3':
                number += '0011'
            if j == '4':
                number += '0100'
            if j == '5':
                number += '0101'
            if j == '6':
                number += '0110'
            if j == '7':
                number += '0111'
            if j == '8':
                number += '1000'
            if j == '9':
                number += '1001'
            if j == 'A':
                number += '1010'
            if j == 'B':
                number += '1011'
            if j == 'C':
                number += '1100'
            if j == 'D':
                number += '1101'
            if j == 'E':
                number += '1110'
            if j == 'F':
                number += '1111'
        numbers = number[::-1]
        # print(numbers)
        now_num = 0
        for k in range(len(number)):
            now_num += (2**k)*int(numbers[k])
        final_list.append(now_num)
    final_list = list(set(final_list))
    # print(final_list)
    final_list.sort(reverse=True)

    print('#{} {}'.format(tc, final_list[K-1]))


