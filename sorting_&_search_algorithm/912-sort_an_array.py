"""
给你一个整数数组 nums，请你将该数组升序排列。

示例 1：
输入：nums = [5,2,3,1]
输出：[1,2,3,5]

示例 2：
输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]
"""


"""思路：插入算法"""


def sortArray(nums):
    for i in range(1, len(nums)):
        pre_idx = i - 1
        curr = nums[i]

        while pre_idx >= 0 and nums[pre_idx] > curr:
            nums[pre_idx+1] = nums[pre_idx]
            pre_idx -= 1
        nums[pre_idx+1] = curr

    return nums

if __name__ == "__main__":
    nums = [5, 1, 1, 2, 0, 0]
    print(sortArray(nums))
