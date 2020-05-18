package main

import (
	"fmt"
	"math"
)

func Decompose(n int64) []int64 {
	// your code
	res := []int64{}
	left := n * n
	n--
	for left > 0 {
		res = append(res, n)
		left -= n * n
		n = int64(math.Sqrt(float64(left)))
	}
	if left == 0 {
		return res
	}
	return []int64{}
}

func main() {
	// dotest(50, []int64{1,3,5,8,49})
	// dotest(5, []int64{3,4})
	// dotest(2, []int64{})
	// dotest(7, []int64{2, 3, 6})
	fmt.Println(Decompose(50))
}
