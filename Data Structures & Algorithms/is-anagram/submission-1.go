func isAnagram(s string, t string) bool {
	if (len(s) == 0 || len(t) == 0) || (len(s) != len(t)) {
		return false
	}
	myS := strings.ToLower(s)
	myT := strings.ToLower(t)

	m := make(map[string]int)
	for _, i := range myS {
		key := string(i)
		m[key]++
	}

	for _, j := range myT {
		key := string(j)
		m[key]--
		if m[key] < 0 {
			return false
		}
	}
	for _, v := range m {
    	if v != 0 {
            return false
        }
    }

	return true

}
