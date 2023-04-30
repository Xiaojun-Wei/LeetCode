# April 29, 2023

"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。

示例 1:
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]

示例 2:
输入: nums = [0]
输出: [0]
"""

"""
时间复杂度: O(n)
"""


def moveZeroes(nums):
    slow = fast = 0
    # 把非0数写到前面
    while fast < len(nums):
        if nums[fast] != 0:
            nums[slow] = nums[fast]
            slow += 1
        fast += 1

    # 把剩下的填0
    while slow < len(nums):
        nums[slow] = 0
        slow += 1
    return nums


nums = [0,1,0,3,12]
print(moveZeroes(nums))

