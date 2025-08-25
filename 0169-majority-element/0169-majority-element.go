func majorityElement(nums []int) int {
    ans := nums[0]
    count := 0
        
    for _, num := range nums {
        if count == 0 {
            ans = num
        }
        if ans == num {
            count++
        } else {
            count--
        }
    }
    count = 0
    for _, num := range nums {
        if num == ans {
            count++
        }
    }
    
    if count > len(nums) / 2{
        return ans
    }

    return -1
}