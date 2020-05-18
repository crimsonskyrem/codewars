package main

import (
	"math"
)

func Solequa(n int) [][]int {
	// your code
	// x2 - 4 * y2 = n
	// y^2 = (x^2 - n)/4
	res := [][]int{}
	// q := int(math.Sqrt(float64(n)))
	// for i := (n + 1) / 2; i >= q; i-- {
	// 	j := int(math.Sqrt(float64(i*i-n))) / 2
	// 	jj := j + j
	// 	if (i-jj)*(i+jj) == n {
	// 		res = append(res, []int{i, j})
	// 	}
	// }
	// i = x + 2y
	// j = x - 2y
	// x = (i+j)/2
	// y = (i-j)/4

	q := int(math.Sqrt(float64(n)))
	for i := 1; i <= q; i++ {
		if n%i == 0 {
			j := n / i
			if (i+j)%2 == 0 && (j-i)%4 == 0 {
				res = append(res, []int{(i + j) / 2, (j - i) / 4})
			}
		}
	}

	return res
}

// func main() {
// 	// dotest(5, [][]int{{3, 1}})
// 	// dotest(12, [][]int{{4, 1}})
// 	// dotest(13, [][]int{{7, 3}})
// 	// dotest(9005, [][]int{{4503, 2251}, {903, 449}})
// 	// dotest(9008, [][]int{{1128, 562}})
// 	// dotest(90002, [][]int{})
// 	fmt.Println(Solequa(90002))
// }
