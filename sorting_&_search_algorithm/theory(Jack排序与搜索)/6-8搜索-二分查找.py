
"""非递归实现"""
def binary_search1(arr, item):
    first, last = 0, len(arr)-1
    while first <= last:
        mid = (first + last) // 2
        if arr[mid] == item:
            return True
        elif item < arr[mid]:
            last = mid-1
        else:
            first = mid+1
    return False


"""递归实现"""
def binary_search2(arr, item):
    if len(arr) == 0:
        return False
    else:
        mid = len(arr) // 2
        if arr[mid] == item:
            return True
        else:
            if item < arr[mid]:
                return binary_search2(arr[:mid], item)
            else:
                return binary_search1(arr[mid+1:], item)



arr = [0, 1, 2, 8, 13, 17, 19, 32, 42]
print(binary_search1(arr, 3))
print(binary_search2(arr, 13))