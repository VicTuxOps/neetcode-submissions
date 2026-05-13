func sortColors(nums []int) {
	low, mid, high := 0, 0, len(nums)-1
	for mid <= high {
		if nums[mid] == 0 {
			nums[low], nums[mid] = nums[mid], nums[low]
			low++
			mid++
		} else if nums[mid] == 1 {
			mid++
		} else if nums[mid] == 2 {
			nums[high], nums[mid] = nums[mid], nums[high]
			high--
		}
	}
/*
	bucketMap := make(map[int]int)
	for _, e := range nums {
		bucketMap[e] = bucketMap[e] + 1
	}
	j := 0
	for l := 0; l <= 2; l++ {
		v, ok := bucketMap[l]
		if !ok {
			continue
		} else {
			for i := 0; i < v; i++ {
				nums[j] = l
				j++
			}
		}
	}
*/
}
