package main

// Complete the FindOutlier function below.
func FindOutlier(integers []int) int {
	odd := make([]int, 0)
	even := make([]int, 0)
	for _, v := range integers {
		if v%2 == 0 {
			even = append(even, v)
			if len(even) > 1 && len(odd) > 0 {
				return odd[0]
			}
		} else {
			odd = append(odd, v)
			if len(odd) > 1 && len(even) > 0 {
				return even[0]
			}
		}

	}
	if len(odd) > 2 {
		return even[0]
	}
	return odd[0]
}

// func main() {
// 	ar := []int{math.MaxInt32, 0, 1}
// 	println(FindOutlier(ar))
// }
