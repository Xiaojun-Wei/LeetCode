class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return x
        left = 1 # 注意
        right = x
        mid = 0 # 注意
        
        while left <= right:
            mid = (left+right)//2
            
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1
            else:
                return mid

        return right # 当left>right的时候return right
        