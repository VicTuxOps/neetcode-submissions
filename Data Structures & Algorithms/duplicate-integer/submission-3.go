func hasDuplicate(nums []int) bool {
	mynumsMap :=  make(map[int]struct{}) //make(map[int]bool)
	for _, e := range nums {
		if _, ok := mynumsMap[e]; ok {
			return true
		} else {
			mynumsMap[e] = struct{}{}
		}
		/*
		if mynumsMap[e] {
			return true
		} else {
			mynumsMap[e] = true
		}
		*/
	}
	return len(mynumsMap) < len(nums)
}
