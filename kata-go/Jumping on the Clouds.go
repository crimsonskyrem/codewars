package main

func jumpingOnClouds(c []int32) int32 {
	l := len(c) - 1
	i := 0
	var count int32 = 0
	for i < l {
		if (i+1) < l && c[i+2] == 0 {
			i += 2
		} else if i < l && c[i+1] == 0 {
			i++
		}
		count++
	}

	return count
}

// func main() {
// 	n := []int32{0, 0, 0, 1, 0, 0}
// 	println(jumpingOnClouds(n))
// }
