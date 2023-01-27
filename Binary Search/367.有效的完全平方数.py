class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 0:
            return 0
        l = 1
        r = num
        mid = 0

        while l <= r:

            mid = (l + r) // 2

            if mid * mid < num:
                l = mid + 1
            elif mid * mid > num:
                r = mid - 1
            else:
                return True

        return False