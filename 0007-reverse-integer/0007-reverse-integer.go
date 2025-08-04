func reverse(x int) int {
    ans := 0
    isNeg := x < 0
    if isNeg {
        x = -x
    }
    for x > 0 {
        if ans > (1<<31-1)/10 || (ans == (1<<31-1)/10 && x%10 > 7) {
            return 0
        }
        ans *= 10
        ans += x % 10
        x = x / 10
    }
    if isNeg{
        return -ans
    }
    return ans
}