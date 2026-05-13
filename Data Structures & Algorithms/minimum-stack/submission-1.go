type MinStack struct {
    stack []int
}

func Constructor() MinStack {
    return MinStack{}
}

func (this *MinStack) Push(val int) {
    this.stack = append(this.stack,val)
}

func (this *MinStack) Pop() {
    this.stack = this.stack[:len(this.stack)-1]
}

func (this *MinStack) Top() int {
    return this.stack[len(this.stack)-1]
}

func (this *MinStack) GetMin() int {
    m := this.stack[0]
    for _, e := range this.stack{
        if e < m{
            m = e
        }
    }
    return m
}
