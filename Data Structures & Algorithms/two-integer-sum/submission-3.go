func twoSum(nums []int, target int) []int {
	myNumsMap := make(map[int]int) //value ; index
	for i, v := range nums {
		diff := target - v
		if j, ok := myNumsMap[diff]; ok {
			return []int{j,i}
		}
		myNumsMap[v] = i
	}
	/*j, i := 0, 1
    for j < len(nums) {
		tmp := nums[j] + nums[i]
		if tmp == target && j != i {
			return []int{j, i}
		}
		i++
		if i == len(nums) {
			j++
			i = j + 1
		}
	}
	*/
	return []int{}
}
