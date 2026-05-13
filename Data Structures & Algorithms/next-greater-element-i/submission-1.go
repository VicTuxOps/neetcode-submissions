func nextGreaterElement(nums1 []int, nums2 []int) []int {
    idx := []int{}
    track := false
	for _, v1 := range nums1 {
        for _, v2 := range nums2 {
            if v1 == v2 {
                idx = append(idx, -1)
                track = true
            }
            if track && v2 > v1 {
                idx = idx[:len(idx)-1]
                idx = append(idx, v2)
                track = false
                fmt.Println(idx)
            }
        }
        track = false
    }
    return idx

}
