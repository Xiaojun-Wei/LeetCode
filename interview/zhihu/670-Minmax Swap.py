"""
给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。

示例 1 :
输入: 2736
输出: 7236
解释: 交换数字2和数字7。

示例 2 :
输入: 9973
输出: 9973
解释: 不需要交换。

注意:
给定数字的范围是 [0, 108]
"""

"""
解题：直接遍历
"""


def maximumSwap(num):
    pivot = num
    num_list = list(str(num))
    for i in range(len(num_list)):
        for j in range(i):
            num_list[i], num_list[j] = num_list[j], num_list[i]
            pivot = max(pivot, int("".join(num_list)))
            num_list[i], num_list[j] = num_list[j], num_list[i]

    return pivot


if __name__ == "__" \
               "main__":
    print(maximumSwap(2736))