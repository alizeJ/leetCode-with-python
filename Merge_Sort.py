def merge_sort(seq) -> list:
    if len(seq) <= 1:
        return seq
    mid = len(seq) // 2
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])
    return merge(left, right)


def merge(left, right) -> list:
    i, j = 0, 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

seq = [5,3,0,6,1,4]
print('排序前：',seq)
result = merge_sort(seq)
print('排序后：',result)