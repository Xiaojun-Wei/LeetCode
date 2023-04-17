"""
给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。


示例 1：
输入：nums = [1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
"""


def findMaxConsecutiveOnes(nums):
    max_num, counter = 0, 0
    for i in nums:
        if i == 1:
            counter += 1
        elif i == 0:
            max_num = counter if max_num > counter else max_num
            counter = 0

    max_num = counter if max_num > counter else max_num
    return max_num


if __name__ == "__name__":
    nums = [1, 1, 0, 1, 1, 1]
    print(findMaxConsecutiveOnes(nums))
