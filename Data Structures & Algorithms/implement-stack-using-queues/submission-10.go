type MyStack struct {
    queue []int
}

func Constructor() MyStack {
    return MyStack{}
}

func (this *MyStack) Push(x int) {
    size := len(this.queue)
    this.queue = append(this.queue, x)
    for range size{
        res := this.queue[0]
        this.queue = append(this.queue[1:], res)
    }
}

func (this *MyStack) Pop() int {
    res := this.queue[0]
    this.queue = this.queue[1:]
    return res
}

func (this *MyStack) Top() int {
    return this.queue[0]
}

func (this *MyStack) Empty() bool {
    if len(this.queue) == 0 {
        return true
    } else {
        return false
    }
}


/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param2 := obj.Pop();
 * param3 := obj.Top();
 * param4 := obj.Empty();
 */
