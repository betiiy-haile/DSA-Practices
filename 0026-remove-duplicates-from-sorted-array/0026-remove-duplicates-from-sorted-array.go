func removeDuplicates(nums []int) int {
    index := 1
    ans := 1

    for index < len(nums) {
        if nums[index] != nums[ans - 1] {
            nums[ans] = nums[index]
            ans += 1
        }
        index += 1
    }
    return ans
}