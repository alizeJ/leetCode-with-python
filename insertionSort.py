def insertionSort(alist):
    for i in range(1, len(alist)):
        j = i - 1
        key = alist[i]
        while j >= 0 and alist[j] > key:
            alist[j+1] = alist[j]
            j -= 1
        alist[j+1] = key


if __name__ == '__main__':
    alist = [2,1,5,3,4,2,7]
    insertionSort(alist)
    print(alist)

