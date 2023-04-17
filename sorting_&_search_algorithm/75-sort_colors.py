# Mar 19, 2023
"""
给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列
我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
必须在不使用库内置的 sort 函数的情况下解决这个问题。

示例 1：
输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]

示例 2：
输入：nums = [2,0,1]
输出：[0,1,2]
"""

"""
方法1：插入排序 O(n^2)
"""


def sortColors1(nums):
    for i in range(1, len(nums)):
        cur = nums[i]
        idx = i - 1
        while idx >= 0 and nums[idx] > cur:
            nums[idx + 1] = nums[idx]
            idx -= 1
        nums[idx + 1] = cur
    return nums


"""
方法2: 单指针交换法: 将0和1交换到前排
"""


def sortColors2(nums):
    p = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i], nums[p] = nums[p], nums[i]
            p += 1
    for j in range(len(nums)):
        if nums[j] == 1:
            nums[j], nums[p] = nums[p], nums[j]
            p += 1
    return nums


if __name__ == "__main__":
    nums = [2, 0, 2, 1, 1, 0]
    print(sortColors2(nums))
