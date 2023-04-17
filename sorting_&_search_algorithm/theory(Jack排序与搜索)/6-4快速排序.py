
def quick_sort(arr, start, end):
    # 递归退出的条件
    if start >= end:
        return

    # 设定起始元素为要寻找位置的基准元素
    mid = arr[start]

    # low为序列左边的由左向右移动的游标
    low = start

    # high为序列右边的由右向做移动的游标
    high = end

    while low < high:
        # 如果low和high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and arr[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        arr[low] = arr[high]

        # 如果low和high未重合，low指向的元素比基准元素小, 则low向右移动
        while low < high and arr[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        arr[high] = arr[low]

    # 退出循环后, low与high重合, 此时所指位置为基准元素的正确位置
    # 将基准元素放到该为该位置
    arr[low] = mid

    # 对基准元素左边的子序列进行快速排序
    quick_sort(arr, start, low-1)

    # 对基准元素右边对子序列进行快速排序
    quick_sort(arr, low+1, end)

    return arr


arr = [54,26,93,17,77,31,44,55,20]
print(quick_sort(arr, 0, len(arr)-1))
