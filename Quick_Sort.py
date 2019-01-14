def quick_sort(seq):
    length = len(seq)
    quick_sort_c(seq, 0, length-1)


def quick_sort_c(seq, left, right):
    if left < right:
        pivot = partition(seq, left, right)

        quick_sort_c(seq, left, pivot-1)
        quick_sort_c(seq, pivot+1, right)


def partition(seq, left, right):
    tmp = seq[left]
    while left < right:
        while left < right and tmp < seq[right]:
            right -= 1
        seq[left] = seq[right]
        while left < right and seq[left] < tmp:
            left += 1
        seq[right] = seq[left]
    seq[left] = tmp
    return left

seq = [5,3,0,6,1,4]
print('排序前：',seq)
quick_sort(seq)
print('排序后：',seq)