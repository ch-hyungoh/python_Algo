for tc in range(1, 1+int(input())):
    cards = list(map(int, input().split()))
    p1 = []
    p2 = []

    p1_list = [0] * 12
    p2_list = [0] * 12

    result = 0
    for i in range(12):
        if i %2 == 0:
            p1.append(cards[i])
        else:
            p2.append(cards[i])

        for a in p1:
            p1_list[a] += 1
        for a in range(10):
            if p1_list[a] == 3 or (p1_list[a] >= 1 and p1_list[a+1] >= 1 and p1_list[a+2] >= 1):
                result = 1
        for a in p1:
            p1_list[a] -= 1
        if result != 0:
            break

        for a in p2:
            p2_list[a] += 1
        for a in range(10):
            if p2_list[a] == 3 or (p2_list[a] >= 1 and p2_list[a+1] >= 1 and p2_list[a+2] >= 1):
                result = 2
        for a in p2:
            p2_list[a] -= 1
        if result != 0:
            break

    print("#{} {}".format(tc, result))