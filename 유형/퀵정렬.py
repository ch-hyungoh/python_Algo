#퀵정렬을 해봅시다!
# 1. partition : 피벗을 기준으로 큰값과 작은값을 분리하는 과정
# 2. 피벗을 기준으로 나누어진 부분을 각각 다시 퀵 정렬 하기
def partition(start,end):
    """
    :start : 분류 대상 시작 인덱스
    :end : 분류 대상 종료 인덱스
    :return: 피벗의 인덱스를 반환
    """
    # 피벗 설정(제일 왼쪽값)
    pivot = arr[start]
    # 큰값과 작은값 을 찾기위한 인덱스i,j 정의
    i = start
    j = end
    # i,j 의 위치가 역전될 때 까지 반복해서 작은값과 큰값의 자리 바꿔주기
    while i <= j:
        # i는 큰값찾을때 까지 오른쪽으로 이동
        while arr[i] <= pivot:
            i += 1
        # j는 작은값을 찾을때 까지 왼쪽으로 이동
        while arr[j] > pivot:
            j -= 1
        # 큰값과 작은 값을 찾았는데, i,j의 위치가 역전 되지 않은 상태면, 큰값이 앞에 있는것
        # 위치를 바꿔줍니다.
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # i,j의 위치가 역전되었으면, 피벗의 위치를 잡아준다.( j위치와 피벗교환)
    arr[start], arr[j] = arr[j], arr[start]
    return j

def quick_sort(start,end):   #시작과 끝점을 정의
    """
    :param arr: 정렬대상배열
    :param start: 정렬 시작 인덱스
    :param end: 정렬 종료 인덱스
    :return:
    """
    # 재귀가 더이상 호출되지 않는 부분을 정의
    if start >= end:
        return
    #1. partition
    pivot_idx = partition(start,end)
    #2. 분할된 부분에 대한 재귀호출
    quick_sort(start,pivot_idx-1)
    quick_sort(pivot_idx+1, end)


for tc in range(1, 1+int(input())):
    N = int(input())
    arr= list(map(int, input().split()))
    quick_sort(0,N-1)
    print(arr)
