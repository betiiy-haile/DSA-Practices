func removeDuplicates(nums []int) int {

    if len(nums) < 2{
        return len(nums)
    }
    index := 2
    ans := 2

    for index < len(nums) {
        if nums[index] == nums[ans - 1] && nums[index] == nums[ans - 2] {
            index += 1
        } else {
            nums[ans] = nums[index]
            index += 1
            ans += 1
        } 
    }

    return ans
}