func nextGreaterElement(nums1 []int, nums2 []int) []int {
    nums1Dict := make(map[int]int)
	for i, v := range nums1 {
        nums1Dict[v] = i
    }

    idx := make([]int, len(nums1))
    for i := range idx {
        idx[i] = -1
    }

    stack := []int{}
    for _, v := range nums2 {
        for len(stack) > 0 && v > stack[len(stack)-1] {
            tmp := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            i := nums1Dict[tmp]
            idx[i] = v
        }


        if _, ok := nums1Dict[v]; ok {
            stack = append(stack, v)
        }
    }
    return idx

}
