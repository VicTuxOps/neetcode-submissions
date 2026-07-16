type Marker struct {
	kind  string
	first int
	second int
	value byte
}

func isValidSudoku(board [][]byte) bool {
	seen := make(map[Marker]struct{})

	for row := 0; row < len(board); row++ {
		for col := 0; col < len(board[row]); col++ {
			element := board[row][col]

			if element == '.' {
				continue
			}

			markers := []Marker{
				{
					kind:  "row",
					first: row,
					value: element,
				},
				{
					kind:  "column",
					first: col,
					value: element,
				},
				{
					kind:   "box",
					first:  row / 3,
					second: col / 3,
					value:  element,
				},
			}

			for _, marker := range markers {
				if _, exists := seen[marker]; exists {
					return false
				}

				seen[marker] = struct{}{}
			}
		}
	}

	return true
}