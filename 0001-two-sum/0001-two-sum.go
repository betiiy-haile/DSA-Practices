func twoSum(nums []int, target int) []int {
    prev := make(map[int]int)
    for i, val := range nums {
        if j, ok := prev[target - val]; ok {
            return []int{j, i}
        }
        prev[val] = i
    }
    return nil
}