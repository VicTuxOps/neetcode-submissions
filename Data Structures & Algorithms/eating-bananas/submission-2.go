func minEatingSpeed(piles []int, h int) int {
		if len(piles) == 0 {
			return 0
		}
		
		maxB := bananas(piles)
		low, high := 1, maxB
		rateB := 1
		out := 1
		for low <= high {
			rateB = (low + high)/2
			if pilesHour(piles, rateB) <= h {
				high = rateB - 1
				out = rateB
			} else if pilesHour(piles, rateB) > h {
				low = rateB + 1
			}
		}
		return out
}

func bananas(b []int) int {
	maxB := 0
	for _, e := range b {
		if e > maxB {
			maxB = e
		}
	}
	return maxB
}

func pilesHour(piles []int, rate int) int {
	out := 0
	for _, e := range piles {
		out = out + ((e+rate-1)/rate)
	}
	return out
}