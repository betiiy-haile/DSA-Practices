class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        diff_count = {}
        
        for i in range(n):
            diff = i - nums[i]
            if diff in diff_count:
                diff_count[diff] += 1
            else:
                diff_count[diff] = 1
        
        total_pairs = n * (n - 1) // 2
        
        valid_pairs = 0
        for count in diff_count.values():
            if count > 1:
                valid_pairs += count * (count - 1) // 2
        
        bad_pairs = total_pairs - valid_pairs
        return bad_pairs