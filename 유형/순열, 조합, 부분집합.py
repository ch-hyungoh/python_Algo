# 순열
# 1. 반복문을 이용
# arr = [1, 2, 3]
# N = 3
# for i1 in range(N):
#     for i2 in range(N):
#         if i2 != i1:
#             for i3 in range(N):
#                if i3 != i2:
#                    print(arr[i1], arr[i2], arr[i3])

# 2. 재귀를 이용한 방법
# sel = [0] * len(arr) # 내가 뽑은 녀석
# check = [0] * len(arr) # 내가 사용한 녀석
# #
# def perm(idx):
#     #1. base case
#     if idx == N:
#         print(sel)
#     #2. recursion case
#     for i in range(len(arr)):
#         if not check[i]:
#             sel[idx] = arr[i]
#             check[i] = 1 # 사용함
#             perm(idx+1)
#             check[i] = 0 # 원상복구
# perm(0)

# 3. 비트를 응용하기
# sel = [0]*N
#
# def perm(idx, check:int):
#     if idx == N:
#         print(sel)
#         return
#     for j in range(N):
#         # 방문 검사하기
#         if check & (1 << j):continue
#         sel[idx] = arr[j] #원소를 사용하지 않았다
#         perm(idx+1, check | (1 << j))
#
# perm(0, 0)

# 4. swap
# def perm(idx):
#     if idx == N:
#         print(arr)
#     else:
#         for i in range(idx, N):
#             arr[idx], arr[i] = arr[i] , arr[idx]
#             perm(idx+1)
#             arr[idx], arr[i] = arr[i], arr[idx]
#
# perm(0)

# 5. np(next_permutaion)

# 6. itertools (라이브러리)

# 조합
# arr = [7, 8, 9, 10]
#
# N = len(arr)
# R = 3
#
# sel = [0] * R

# idx : 원본배열의 인덱스
# s_idx : 내가 지금 뽑고 있는 위치

# def comb(idx, s_idx):
#     if s_idx == R:
#         print(sel)
#     elif idx == N:
#         return
#     else:
#         sel[s_idx] = arr[idx]
#         comb(idx+1, s_idx+1)
#         comb(idx+1, s_idx)

# def comb2(idx, s_idx):
#     if s_idx == R:
#         print(sel)
#         return
#
#     for i in range(idx, N):
#         sel[s_idx] = arr[i]
#         comb2(i+1, s_idx+1)
#
# # 경계를 결정해주는 것
# def comb3(idx, s_idx):
#     if s_idx ==R:
#         print(sel)
#         return
#
#     for i in range(idx, N-R+s_idx+1):
#         sel[s_idx] = arr[i]
#         comb3(i+1, s_idx+1)
# comb2(0, 0)

# comb3(0, 0)
# comb(0, 0)


# 부분집합