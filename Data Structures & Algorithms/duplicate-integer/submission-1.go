func hasDuplicate(nums []int) bool {
	mynumsMap := make(map[int]bool)
	for _, e := range nums {
		if mynumsMap[e] {
			return true
		} else {
			mynumsMap[e] = true
		}
	}
	return false
}
