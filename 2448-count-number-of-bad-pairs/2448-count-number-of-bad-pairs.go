func countBadPairs(nums []int) int64 {
    n := len(nums)
	diffCount := make(map[int]int)

	for i := 0; i < n; i++ {
		diff := i - nums[i]
		diffCount[diff]++
	}

	totalPairs := n * (n - 1) / 2

	validPairs := 0
	for _, count := range diffCount {
		if count > 1 {
			validPairs += count * (count - 1) / 2
		}
	}

	badPairs := totalPairs - validPairs
	return int64(badPairs)

}