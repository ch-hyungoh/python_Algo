for tc in range(1, 1+int(input())):
    n, m = map(int,input().split())
    m_list = []
    while m > 0:
        m_list.insert(0, m % 2)
        m = m // 2
    if len(m_list) < n:
        while len(m_list) <= n:
            m_list.insert(0, 0)

    result = True
    for i in range(n):
        if m_list.pop() == 0:
            result = False

    if result:
        print('#{} ON'.format(tc))
    else:
        print('#{} OFF'.format(tc))