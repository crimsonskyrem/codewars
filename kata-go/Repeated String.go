package main

func repeatedString(s string, n int64) int64 {

	a, b := int64(0), int64(0)
	c := n / int64(len(s))
	d := n % int64(len(s))
	for i := 0; i < len(s); i++ {
		if s[i] == 'a' {
			a++
		}
	}
	for i := int64(0); i < d; i++ {
		if s[i] == 'a' {
			b++
		}
	}

	return (a * c) + b
}

// func main() {
// 	var n int64
// 	s := "abcac"
// 	n = 10

// 	println(repeatedString(s, n))
// }
