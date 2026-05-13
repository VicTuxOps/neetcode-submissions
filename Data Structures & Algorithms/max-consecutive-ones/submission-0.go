func findMaxConsecutiveOnes(nums []int) int {
    cnt := 0
    finalCnt := 0
    for _, e := range nums {
        if e == 1 {
            cnt++
        } else {
            cnt = 0
        }
        if cnt > finalCnt {
            finalCnt = cnt
        }
    }
    return finalCnt
}
