// Definition for a pair.
// type Pair struct {
//     Key   int
//     Value string
// }

func insertionSort(pairs []Pair) [][]Pair {
    if len(pairs) == 0 {
        return [][]Pair{}
    }
    out := append([][]Pair{}, append([]Pair(nil), pairs...))
    for i := 1; i < len(pairs); i++ {
        tmpIdx := i
        for tmpIdx > 0 && pairs[tmpIdx].Key < pairs[tmpIdx-1].Key {
            tmpval := pairs[tmpIdx-1]
            pairs[tmpIdx-1] = pairs[tmpIdx]
            pairs[tmpIdx] = tmpval
            tmpIdx--
        }
        out = append(out, append([]Pair(nil), pairs...))
    }
    return out
}
