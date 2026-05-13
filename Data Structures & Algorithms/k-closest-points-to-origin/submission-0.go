// An IntHeap is a min-heap of ints.
type IntHeap [][]int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i][1] < h[j][1] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x any) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.([]int))
}

func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func kClosest(points [][]int, k int) [][]int {
	out := [][]int{}
	closeHeap := &IntHeap{}
	heap.Init(closeHeap)

	for i := range points {
		x := points[i][0]
		y := points[i][1]
		dist := int(math.Ceil(math.Sqrt(math.Pow(float64(x),2) + math.Pow(float64(y),2))))
		e := []int{i, dist}
		heap.Push(closeHeap, e)
	}

	j := 0
	for j < k {
		ans := (*closeHeap)[0]
		fmt.Println(ans)
		heap.Pop(closeHeap)
		out = append(out, points[ans[0]])
		j++
	}

	return out

}
