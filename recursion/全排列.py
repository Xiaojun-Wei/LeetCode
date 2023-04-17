"""
给定一个不含重复数字的数组 ，返回其所有可能的全排列
"""

# def enumerate(arr):
#     if len(arr) <= 1:
#         return arr
#     out = []
#
#     def recur(pivot, left):
#         if left == 0:
#             out.append(pivot)
#         for i, j in enumerate(left):
#             recur(pivot+[j], left[:i] + left[i+1:])
#     recur([], arr)
#     return out



def enumerate_all(nums):
    if len(nums) <= 1:
        return nums
    out = []
    def recursion(pivot, rest):
        if len(rest) == 0:  # base情况
            out.append(pivot)
        for i, n in enumerate(rest):
            recursion(pivot+[n], rest[:i] + rest[i+1:])

    recursion([], nums)
    return out

print(enumerate_all([1,2,3]))


# if __name__ == "__main__":
#     print(enumerate([1,2,3]))
