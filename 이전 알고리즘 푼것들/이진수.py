for tc in range(1, 1+int(input())):
    n, m = input().split()

    num_list = []
    reulst =''
    for i in range(int(n)):
        num = m[i]
        if num == 'A':
            num = 10
        elif num == 'B':
            num = 11
        elif num == 'C':
            num = 12
        elif num == 'D':
            num = 13
        elif num == 'E':
            num = 14
        elif num == 'F':
            num = 15
        else:
            num = int(num)
        num_list.append(num)

    for i in range(int(n)):
        now = num_list[i]
        now_num = []
        while now > 0:
            now_num.insert(0, now % 2)
            now = now // 2
        if len(now_num) < 4:
            while len(now_num) < 4:
                now_num.insert(0, 0)
        for k in range(4):
            reulst += str(now_num[k])
    print("#{} {}".format(tc,reulst))