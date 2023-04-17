
def selection_sort(arr):
    n = len(arr)
    # 需要进行 n-1 次选择操作
    for i in range(n-1):
        # 记录最小位置
        min_idx = i
        # 从i+1位置到末尾选择出最小数据
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # 如果选择出的数据不在正确位置，进行交换
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


print(selection_sort([54,226,93,17,77,31,44,55,20]))
