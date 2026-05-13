func searchMatrix(matrix [][]int, target int) bool {
	if len(matrix) == 0 || (len(matrix) == 1 && len(matrix[0]) == 0) {
		return false
	}

	for _, row := range matrix {
		lp, rp := 0, len(row) - 1
		for lp <= rp {
			mp := (lp + rp)/2
			if row[mp] > target {
				rp = mp - 1
			} else if row[mp] < target {
				lp = mp + 1
			} else {
				return true
			}
		}
	}
	return false
}
