// Definition for a pair.
// type Pair struct {
//     Key   int
//     Value string
// }

/*
type Solution struct {

}

func NewSolution() *Solution {

}
*/

func QuickSort(pairs []Pair) []Pair {
	k := len(pairs)
	if k <= 1 {
		return pairs
	}
	pivot := pairs[k-1]
	e := 0
	for i:= 0; i < k-1; i++ {
		if pairs[i].Key < pivot.Key {
			tmp := pairs[e]
			pairs[e] = pairs[i]
			pairs[i] = tmp
			e++
		}
	}
	pairs[k-1] = pairs[e]
	pairs[e] = pivot
	QuickSort(pairs[:e])
	QuickSort(pairs[e+1:])

	return pairs
}
