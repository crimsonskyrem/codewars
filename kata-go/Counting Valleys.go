package main

func countingValleys(n int32, s string) int32 {
	var sea, count, last, i int32
	sea = 0
	count = 0
	i = 0
	for i < n {
		if s[i] == 85 {
			sea++
		}
		if s[i] == 68 {
			sea--
		}
		if sea == 0 && last == -1 {
			count++
		}
		last = sea
		i++
	}

	println(count)
	return count
}

// func main() {
// 	s := "UDDDUDUUDU"
// 	var n int32 = 10
// 	countingValleys(n, s)
// }
