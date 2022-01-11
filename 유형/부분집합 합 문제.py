N = 10
arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]

for i in range(2**N): # 2** N : 1<<N
    #i의 비트모양을 이용하여 모든 부분집합을 구하낟.
    # subset_sum = 0
    subset = []
    for j in range(N):
        # J : 확인할려는 비트의 순서
        if (i & ( 1 << j )) == 1:
            #i의 j번째 비트가 1이다 ; arr 의 j번째 요소가 부분집합에 포함된다
            # subset_sum += arr[j]
            subset.append(arr[j])
    if sum(subset) == 0:
        print(subset)


