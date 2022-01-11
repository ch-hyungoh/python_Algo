def pool(cost, m):
    global money

    if m > 12:
        if money > cost:
            money = cost
        return
    pool(cost + d * month[m], m+1)

    pool(cost + m1, m + 1)

    pool(cost + m3, m + 3)

for test in range(1, 1+int(input())):
    d, m1, m3, y = map(int,input().split()) # d 1일 m1 1달 m3 3달 y 1년

    month = [0]+list(map(int, input().split()))

    money = y

    pool(0, 1)

    print("#{} {}".format(test, money))