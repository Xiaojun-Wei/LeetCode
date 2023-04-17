

def insert_sort(arr):
    # 从第二个位置，即下表为1的元素开始向前插入
    for i in range(1, len(arr)-1):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr


print(insert_sort([54,26,93,17,77,31,44,55,20]))