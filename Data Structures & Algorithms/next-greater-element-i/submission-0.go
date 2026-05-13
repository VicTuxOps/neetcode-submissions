func nextGreaterElement(nums1 []int, nums2 []int) []int {
    idx := []int{}
    track := false
	for _, v1 := range nums1 {
        for _, v2 := range nums2 {
            fmt.Println("From nums1: ", v1)
            fmt.Println("From nums2: ", v2)
            if v1 == v2 {
                fmt.Println("These are equal", v1)
                idx = append(idx, -1)
                track = true
            }
            if track && v2 > v1 {
                fmt.Println("It is bigger: ", v2)
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
