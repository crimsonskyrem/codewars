package main

func Going(n int) float64 {
	// your code
	res := float64(1)
	last := res
	for i := 0; i < n-1; i++ {
		last *= (1 / float64(n-i))
		res += last
	}
	return float64(int64(res*1000000)) / 1000000
}

// func main() {
// 	// dotest(5, 1.275)
// 	// dotest(6, 1.2125)
// 	// dotest(7, 1.173214)
// 	// dotest(8, 1.146651)
// 	fmt.Println(Going(5))
// }
