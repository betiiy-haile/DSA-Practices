class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 7 6 5   4 3 2 1
        # 5 6 7   1 2 3 4 
        k = k % len(nums)
        nums.reverse()
        left = 0
        right = k - 1
        while left <= right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1

        left = k
        right = len(nums) - 1
        while left <= right:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -= 1

        
        