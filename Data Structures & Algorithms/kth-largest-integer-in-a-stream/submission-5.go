type KthLargest struct {
	OrderArr *IntHeap
	SizeArr  int
}

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] < h[j] } // Min-heap
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func Constructor(k int, nums []int) KthLargest {
	h := KthLargest{
		OrderArr: &IntHeap{},
		SizeArr: k,
	}
	heap.Init(h.OrderArr)

	for _, val := range nums {
		heap.Push(h.OrderArr, val)
		if h.OrderArr.Len() > k {
			heap.Pop(h.OrderArr)
		}
	}
	h.SizeArr = k

	return h
}


func (this *KthLargest) Add(val int) int {
    heap.Push(this.OrderArr, val)
	if this.OrderArr.Len() > this.SizeArr {
		heap.Pop(this.OrderArr)
	}
	if len(*this.OrderArr) > 0 {
		return (*this.OrderArr)[0]
	}
	return -1
}
