func maxProfit(prices []int) int {
    profit := 0
    left := 0

    for right := range(len(prices)) {
        if prices[right] <= prices[left]{
            left = right
        }
        profit = max(profit, prices[right] - prices[left])
    }

    return profit
}