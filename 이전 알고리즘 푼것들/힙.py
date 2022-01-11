def enq(n):
    global last
    last += 1
    tree[last] = n
    c= last
    p = c//2
    while p >= 1 and tree[p] < tree[c]:
        tree[p], tree[c] =  tree[c],  tree[p]
        c = p
        p = c//2

def dep():
    global last
    tmp = tree[1]
    tree[1] = tree[last]
    p = 1
    c1 = 2*p
    c2 = 2*p+1
    while c1<= last: #자식이 하나라도 있으면
        if c2 <= last: #자식이 2인경우
            if tree[c1] > tree[c2] and tree[c1]>tree[p]:
                tree[c1], tree[p] = tree[p], tree[c1]
            elif tree[c1] < tree[c2] and tree[c2]>tree[p]:
                tree[c2], tree[p] = tree[p], tree[c2]
                p = c2
            c1 = p*2
            c2 = p*2+1
        else: # 왼쪽자식만 있는경우
            if tree[c1]>tree[p]:
                tree[c1], tree[p] = tree[p], tree[c1]
                break

tree = [0]*101
last = 0
a = [7, 2, 3, 9, 5]
for x in a:
    enq(x)