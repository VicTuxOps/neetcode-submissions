// An IntHeap is a min-heap of ints.
type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x any) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() any {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func lastStoneWeight(stones []int) int {
	if len(stones) == 0 {
		return -1
	}

	groupedStones := &IntHeap{}
	for _, r := range stones {
		heap.Push(groupedStones, r)
	}

	for groupedStones.Len() > 1 {
		max1 := heap.Pop(groupedStones)
		max2 := heap.Pop(groupedStones)
		diff := max1.(int) - max2.(int)
		if diff > 0 {
			heap.Push(groupedStones, diff)
		}
	}

	if groupedStones.Len() == 0 {
		return 0
	}

	return heap.Pop(groupedStones).(int)
}
