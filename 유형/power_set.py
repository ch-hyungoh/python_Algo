#공집합과 자기자신을 포함한 모든 부분집합
# 해당원소가 있거나 없거나 둘중 하나라 2^n개

# N = 4
# arr = [-1, 3, -9, 6]

# selected = [0] * N
#
# def power_set(idx):
#     if idx == N: # 모든 요소에 대해서 부분집합 포함 여부를 결정
#         #선택된 요소들의 합 구하기
#         subset = []
#         for i in range(N):
#             if selected[i] == 1:
#                 subset.append(arr[i])
#         if sum(subset) == 0:
#             print(subset)
#     for i in range(2):
#         selected[idx] = i
#         power_set(idx+1)
#
# power_set(3)

# 1. 반복문으로 만드는 법
# 원소수 만큼 반복문이 필요함


# for i in range(1 << N): # 2를 N번 곱한다.
#     # i 가 부분집합인것은 알겠다. 그런데 어떤 원소를 가진 부분 집합인가?
#     for j in range(N): # N번 검사를 하겠다.
#         if i & 1 << j: # i 의 j 번째 비트의 값이 있는지를 확인
#             print(arr[j], end=" ")
#     print()

# 2. 재귀를 이용한 방법
arr = [4, 5, 6]
N = len(arr)

sel = [0]* N

# def powerset(idx):
#     # 1.base case
#     if idx == N:
#         print(sel)
#         for i in range(N):
#             if sel[i]:
#                 print(arr[i], end=' ')
#         print()
#         return
#     # recursion case
#     sel[idx] = 0
#     powerset(idx + 1)
#     sel[idx] = 1
#     powerset(idx + 1)




def powerset(idx):
    # 1.base case
    if idx == N:
        print(sel)
    else:
        for i in range(2):
            sel[idx] = i
            powerset(idx +1)

powerset(0)