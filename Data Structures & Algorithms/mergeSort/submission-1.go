func mergeSort(pairs []Pair) []Pair {
    sPair := len(pairs)
    if sPair <= 1 {
        return pairs
    }
    divide := sPair/2
    a := mergeSort(pairs[:divide])
    b := mergeSort(pairs[divide:])
    
    res := make([]Pair, 0, sPair)
    i, j := 0, 0
    for i < len(a) && j < len(b) {
        if a[i].Key <= b[j].Key {
            res = append(res, a[i])
            i++
        } else {
            res = append(res, b[j])
            j++
        }
    }
    res = append(res, a[i:]...)
    res = append(res, b[j:]...)

    return res
}