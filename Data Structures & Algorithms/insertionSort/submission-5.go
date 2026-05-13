// Definition for a pair.
// type Pair struct {
//     Key   int
//     Value string
// }

func insertionSort(pairs []Pair) [][]Pair {
    res := [][]Pair{}
    npairs := len(pairs)
    if npairs == 0 {
        return res
    }
    res = append(res, append([]Pair(nil), pairs...))
    for i := 1; i < npairs; i++ {
        tmpIdx := i
        for tmpIdx > 0 && pairs[tmpIdx].Key < pairs[tmpIdx-1].Key {
            pairs[tmpIdx-1], pairs[tmpIdx] = pairs[tmpIdx], pairs[tmpIdx-1]
            tmpIdx--
        }
        pairCopy := make([]Pair, len(pairs))
        copy(pairCopy, pairs)
        res = append(res, pairCopy)
    }
    return res
}
