"""
学校打算为全体学生拍一张年度纪念照。根据要求，学生需要按照 非递减 的高度顺序排成一行。
排序后的高度情况用整数数组 expected 表示，其中 expected[i] 是预计排在这一行中第 i 位的学生的高度（下标从 0 开始）。
给你一个整数数组 heights ，表示 当前学生站位 的高度情况。heights[i] 是这一行中第 i 位学生的高度（下标从 0 开始）。
返回满足 heights[i] != expected[i] 的 下标数量 。

示例：
输入：heights = [1,1,4,2,1,3]
输出：3

解释：
高度：[1,1,4,2,1,3]
预期：[1,1,1,2,3,4]
下标 2 、4 、5 处的学生高度不匹配。
"""


def heightChecker(heights):
    differ = 0
    heights_num = [0] * max(heights)
    heights_sorted = list()
    for h in heights:
        heights_num[h-1] += 1

    for i in range(len(heights_num)):
        heights_sorted += [i+1] * heights_num[i]

    for j in range(len(heights_sorted)):
        if heights_sorted[j] != heights[j]:
            differ += 1

    return differ


if __name__ == "__main__":
    heights = [1, 1, 4, 2, 1, 3]
    print(heightChecker(heights))

