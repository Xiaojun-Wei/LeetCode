## Complexity ##
time complexity: O(log(n))
space complexity: O(1)

## Template ##
**Python**
```Python

def search(self, nums: List[int], target: int) -> int:
    left, right = 0, len(nums)-1
    
    while left <= right:
        mid = (left+right)//2
        if nums[mid] > target: 
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else: # 
            return mid
    return -1
```
**Java**

without recursion
```Java
public int binarySearch(int array[], int target) {
    int left = 0;
    int right = array.length - 1;
    while(left <= right) {  
        int mid = left + (right - left) / 2;  
        if (array[mid] == target) { 
            return mid;
        } else if (target < array[mid]) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return -1;
}
```
with recursion
```Java
public int search(int nums[], int start, int end, int target) {
    if(end >= start) {
        int mid = start + (end - start) / 2;
        if(nums[mid] == target) {
            return mid;
        } else if (target < nums[mid]) {
            return search(nums, start, mid - 1, target);
        } 
        return search(nums, mid + 1, end, target);
    }
    return -1;
}
```

## LeetCode ##
2023-01-27
- 33.搜索旋转排序数组 Search in Rotated Sorted Array (Medium, Array, Python)
- 35.搜索插入位置 Search Insert Position (Easy, Array, Java)
- 69.x的平方根 Sqrt(x) (Easy, Array, Python)
- 367.有效的完全平方数 Valid Perfect Square (Easy, Array, Python)
- 704.二分查找 Binary Search (Easy, Array, Java)

2023-01-28
- 34.在排数组中查找元素的第一个和最后一个位置 Find First and Last Position of Element in Sorted Array
- 162. Find Peak Element
- 74.
- 540.
- 744.