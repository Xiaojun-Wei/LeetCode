"""
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

示例 1:
输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

示例 2:
输入: nums = [1], k = 1
输出: [1]
"""


def topKFrequent(nums, k):
    dic = {}  # key:num, value: freq
    for i in range(len(nums)):
        if nums[i] not in dic:
            dic[nums[i]] = 1
        else:
            dic[nums[i]] += 1

    res = []

    while k > 0:
        tmp = 0
        for num in dic:
            if dic[num] > tmp:
                tmp = dic[num]
                top = num
        dic[top] = -1
        res.append(top)
        k -= 1
    return res


if __name__ == "__main__":
    print(topKFrequent([1,1,1,2,2,3], 2))
