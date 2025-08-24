class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = 0
        index = 0

        while index < len(nums):
            if nums[index] != val:
                nums[ans] = nums[index]
                ans += 1
            index += 1
        return ans