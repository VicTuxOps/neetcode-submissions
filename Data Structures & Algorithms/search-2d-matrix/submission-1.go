func searchMatrix(matrix [][]int, target int) bool {
	if len(matrix) == 0 || (len(matrix) == 1 && len(matrix[0]) == 0) {
		return false
	}

	var movePLeft bool
	lpm, rpm := 0, len(matrix)-1
	for lpm <= rpm {
		mpm := (lpm + rpm)/2
		myrow := matrix[mpm]
		lp, rp := 0, len(myrow) - 1
		for lp <= rp {
			mp := (lp + rp)/2
			if myrow[mp] > target {
				rp = mp - 1
				movePLeft = true
			} else if myrow[mp] < target {
				lp = mp + 1
				movePLeft = false
			} else {
				return true
			}
		}
		if movePLeft {
			rpm = mpm - 1
		} else {
			lpm = mpm + 1
		}
	}

	/*
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
	*/
	return false
}
