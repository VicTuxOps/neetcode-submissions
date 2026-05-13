type MinStack struct {
    minNum []int
    stack []int
}

func Constructor() MinStack {
    return MinStack{
        stack: []int{},
        minNum: []int{},
    }
}

func (this *MinStack) Push(val int) {
    this.stack = append(this.stack,val)
    if len(this.minNum) == 0{
        this.minNum = append(this.minNum,val)
    } else {
        tmp := this.minNum[len(this.minNum)-1]
        if val < tmp{
            this.minNum = append(this.minNum,val)
        } else {
            this.minNum = append(this.minNum, tmp)
        }
    }
}

func (this *MinStack) Pop() {
    this.stack = this.stack[:len(this.stack)-1]
    this.minNum = this.minNum[:len(this.minNum)-1]
}

func (this *MinStack) Top() int {
    return this.stack[len(this.stack)-1]
}

func (this *MinStack) GetMin() int {
    m := this.minNum[len(this.minNum)-1]
    return m
}
