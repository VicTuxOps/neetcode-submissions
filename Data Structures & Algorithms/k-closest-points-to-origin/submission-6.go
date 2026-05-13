// Max-heap by dist at [0]
type IntHeap [][]int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i][0] > h[j][0] } // compare dist
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x any) { *h = append(*h, x.([]int)) }

func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[:n-1]
	return x
}

func kClosest(points [][]int, k int) [][]int {
	if k > len(points) {
		k = len(points)
	}

	h := &IntHeap{}
	for _, p := range points {
		dist := p[0]*p[0] + p[1]*p[1]
		if h.Len() < k {
			heap.Push(h, []int{dist, p[0], p[1]})
		} else if dist < (*h)[0][0] {
			heap.Pop(h)
			heap.Push(h, []int{dist, p[0], p[1]})
		}
	}

	out := make([][]int, 0, k)
	for h.Len() > 0 {
		item := heap.Pop(h).([]int)
		out = append(out, []int{item[1], item[2]})
	}
	return out
}