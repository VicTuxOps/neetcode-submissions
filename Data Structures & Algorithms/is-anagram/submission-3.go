func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    m := make(map[rune]int)

    for _, r := range s {
        m[r]++
    }

    for _, r := range t {
        m[r]--
        if m[r] < 0 {
            return false
        }
    }

    return true
}