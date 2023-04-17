
def shell_sort(arr):
    n = len(arr)
    # 初始步长
    gap = n / 2
    while gap > 0:
        for i in range(gap, n):
            j = i
            # 插入排序
            while j>= gap and arr[j-gap] > arr[j]:
                arr[j-gap], arr[j] = arr[j], arr[j-gap]
                j -= gap
        # 得到新步长
        gap = gap/2
    return arr


arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(shell_sort(arr))