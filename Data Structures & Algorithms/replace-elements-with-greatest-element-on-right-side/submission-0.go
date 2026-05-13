func replaceElements(arr []int) []int {
	maxVal := -1
	for i := len(arr)-1; i >= 0 ; i-- {
		temp := arr[i]
		arr[i] = maxVal
		if temp > maxVal {
			maxVal = temp
		}
	}
	return arr
}
