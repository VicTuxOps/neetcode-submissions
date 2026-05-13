func search(nums []int, target int) int {
	sizeNums := len(nums)
	if sizeNums == 0 {
		return -1
	}
	if sizeNums == 1 {
		if nums[0] == target {
			return  0
		} else {
			return -1
		}
	}

	l, r := 0, sizeNums-1
	for l <= r {
		m := (l+r)/2
		if nums[m] > target {
			r = m - 1
		} else if nums[m] < target {
			l = m + 1
		} else {
			return m
		}
	}
	return -1
}
