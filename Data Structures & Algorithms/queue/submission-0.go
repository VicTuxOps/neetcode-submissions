type Node struct {
    Val int
    Next *Node
    Prev *Node
}

type Deque struct {
    Head *Node
    Tail *Node
    Size int
}

func NewDeque() Deque {
    return Deque{}
}

func (d *Deque) IsEmpty() bool {
    return d.Size == 0
}

func (d *Deque) Append(value int) {
    newElement := &Node{Val: value}
    if d.Size == 0 {
        d.Head = newElement
        d.Tail = newElement
    } else {
        newElement.Prev = d.Tail
        d.Tail.Next = newElement 
        d.Tail = newElement
    }
    d.Size++
}

func (d *Deque) AppendLeft(value int) {
    newElement := &Node{Val: value}
    if d.Size == 0 {
        d.Head = newElement
        d.Tail = newElement
    } else {
        newElement.Next = d.Head
        d.Head.Prev = newElement
        d.Head = newElement
    }
    
    d.Size++
}

func (d *Deque) Pop() int {
    if d.Size == 0 {
        return -1
    }
    tailVal := d.Tail.Val
    if d.Size == 1 {
        d.Head = nil
        d.Tail = nil
        d.Size = 0
        return tailVal
    }
    prevNode := d.Tail.Prev
    d.Tail.Prev = nil
    prevNode.Next = nil
    d.Tail = prevNode
    d.Size--
    return tailVal
}

func (d *Deque) PopLeft() int {
    if d.Size == 0 {
        return -1
    }
    headVal := d.Head.Val
    if d.Size == 1 {
        d.Head = nil
        d.Tail = nil
        d.Size = 0
        return headVal
    }

    nextNode := d.Head.Next
    d.Head.Next = nil
    nextNode.Prev = nil
    d.Head = nextNode
    d.Size--
    return headVal
}
