def partition(arr, start, end):
    '''

    :param start: 분류 대상 시작 인덱스
    :param end: 분류 대상 종료 인덱스
    :return: 피벗의 인덱스를 반환함함
   '''
    return 0

def quick_sort(arr,start,end):
    '''

    :param arr: 정렬대상배역
    :param start:  정렬 시작 인덱스
    :param end: 정렬 종료 인덱스
    :return:
    '''

    # 1.partition
    pivot_inx = partition(arr, start, end)
    quick_sort(arr,start,pivot_inx-1)
    quick_sort(arr, pivot_inx+1, end)