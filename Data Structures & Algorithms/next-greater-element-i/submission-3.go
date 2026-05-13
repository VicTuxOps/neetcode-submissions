func nextGreaterElement(nums1 []int, nums2 []int) []int {
    nums1Dict := make(map[int]int)
	for i, v := range nums1 {
        nums1Dict[v] = i
    }

    idx := make([]int, len(nums1))
    for i := range idx {
        idx[i] = -1
    }

    for i, v := range nums2 {
        if _, ok := nums1Dict[v]; !ok {
            continue
        }
        for j := i + 1; j < len(nums2); j++ {
            if nums2[j] > nums2[i] {
                myIdx := nums1Dict[nums2[i]]
                idx[myIdx] = nums2[j]
                break
            }
        }
    }
    return idx

}
