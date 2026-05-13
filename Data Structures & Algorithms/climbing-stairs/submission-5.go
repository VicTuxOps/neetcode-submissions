var m = make(map[int]int)

func climbStairs(n int) int {
    if n <=2 {
        return n
    }

    //out := 0
    if val, ok := m[n]; ok {
        return val
    }
    out := climbStairs(n-2) + climbStairs(n-1)// + out
    m[n] = out
    return out
}
