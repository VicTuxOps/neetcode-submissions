func anagramMappings(nums1 []int, nums2 []int) []int {
	var dictNums = make(map[int]int)
	listOut := []int{}
	for i, e := range nums2 {
		dictNums[e] = i
	}

	for _, e := range nums1 {
		idx := dictNums[e]
		listOut = append(listOut, idx)
	}
	return listOut
}
