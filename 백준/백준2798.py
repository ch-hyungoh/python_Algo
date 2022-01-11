def blackjac(now, numbers, puls):
    global max_puls

    if numbers == 3:
        if puls <= M:
            if puls > max_puls:
                max_puls = puls
        return

    if puls >= M:
        return

    if now == N:
        return

    if used_list[now] == 0:
        puls += card_list[now]
        used_list[now] = 1
        blackjac(now+1, numbers+1, puls)
        used_list[now] = 0
        blackjac(now+1, numbers, puls-card_list[now])
    else:
        blackjac(now+1, numbers, puls)


N, M = map(int, input().split())

card_list = list(map(int, input().split()))

used_list = [0]*N

max_puls = 0

blackjac(0, 0, 0)

print(max_puls)

