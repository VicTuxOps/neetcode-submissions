func hasDuplicate(nums []int) bool {
	mynumsMap := make(map[int]int)
	for _, e := range nums {
		if _, ok := mynumsMap[e]; ok {
			return true
		} else {
			mynumsMap[e] = 1
		}
	}
	return false
}
