func countStudents(students []int, sandwiches []int) int {
    hungryStudents := len(students)
    typeStudents := make([]int, 2)

    for _, students := range students {
        typeStudents[students] += 1
    }

    for _, s := range sandwiches {
        if typeStudents[s] > 0 {
            typeStudents[s]-=1
            hungryStudents-=1
        } else {
            break
        }
    }

    return hungryStudents
}