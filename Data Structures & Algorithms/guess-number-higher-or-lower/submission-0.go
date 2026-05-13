/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * func guess(num int) int;
 */

func guessNumber(n int) int {
    low, high := 0, n
	for low <= high {
		myGuess := (low+high)/2
		if guess(myGuess) == -1 {
			high = myGuess - 1
		} else if guess(myGuess) == 1 {
			low = myGuess + 1
		} else {
			return myGuess
		}
	}
	return 0
}
