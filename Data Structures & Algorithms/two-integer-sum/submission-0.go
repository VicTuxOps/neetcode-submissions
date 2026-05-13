func twoSum(nums []int, target int) []int {
	j, i := 0, 1
    for j < len(nums) {
		fmt.Println(j)
		fmt.Println(i)
		tmp := nums[j] + nums[i]
		if tmp == target && j != i {
			return []int{j, i}
		}
		i++
		if i == len(nums) {
			fmt.Println("J!")
			j++
			i = j + 1
		}
	}
	return []int{}
}
