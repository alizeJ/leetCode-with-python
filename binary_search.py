def binary_search(seq, target, start=0, end=None):
    if end is None:
        end = len(seq) - 1

    while start <= end:
        mid = (start + end) // 2
        if seq[mid] < target:
            start = mid + 1
        elif seq[mid] > target:
            end = mid - 1
        else:
            return mid
    return -1

# 查找最后一个等于给定值的元素


def binary_search02(seq, length, value):
    start = 0
    end = length - 1
    while start <= end:
        mid = start + ((end - start) >> 1)
        if seq[mid] > value:
            end = mid - 1
        elif seq[mid] < value:
            start = mid + 1
        else:
            if mid == end or seq[mid+1] != value:
                return mid
            else:
                start = mid + 1


#查找第一个大于等于给定值的元素


def binary_search03(seq, length, value):
    start = 0
    end = length - 1
    while start <= end:
        mid = start + ((end - start) >> 1 )
        if value > seq[mid]:
            start = mid + 1
        elif seq[mid] >= value:
            if mid == 0 or seq[mid-1] < value:
                return mid
            else:
                end = mid - 1

    return -1
