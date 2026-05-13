func validWordSquare(words []string) bool {
	for i, word := range words {
		for j := 0; j < len(word); j++ {
			if j >= len(words) || i >= len(words[j]) || word[j] != words[j][i] {
				return false
			}
		}
	}
	return true
}