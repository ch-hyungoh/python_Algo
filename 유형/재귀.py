def ncr(n,r,s,k):
    if k == r:
        print(*comb)
    else:
        for i in range(s, n-r+k+1):
            comb[k] = i
            ncr(n, r, i+1, k+1)

N = 10
R = 3
comb = [0]*R
ncr(N,R,0,0)