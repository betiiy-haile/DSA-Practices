func removeElement(nums []int, val int) int {
    ans := 0
    index := 0

    for index < len(nums) {
        if nums[index] != val {
            nums[ans] = nums[index]
            ans += 1
        }
        index += 1
    }

    return ans
}