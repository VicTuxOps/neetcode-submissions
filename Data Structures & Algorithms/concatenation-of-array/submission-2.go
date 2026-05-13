func getConcatenation(nums []int) []int {
    ans := []int{}
    for i := 0; i<2 ; i++{
        ans = append(ans,nums[0:]...)
    }
    return ans
}
