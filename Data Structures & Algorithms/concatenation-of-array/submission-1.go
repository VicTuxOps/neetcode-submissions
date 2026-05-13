func getConcatenation(nums []int) []int {
    ans := []int{}
    ans = append(nums[0:],nums[0:]...)
    return ans
}
