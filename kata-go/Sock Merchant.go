package main

// Complete the sockMerchant function below.
func sockMerchant(n int32, ar []int32) int32 {
	// pair := []int32{}
	var count int32
	count = 0

	pair := ar[:1]
	new := ar[1:]
	for _, v := range new {
		flag := true
		for j, m := range pair {
			if m == v {
				pair = append(pair[:j], pair[j+1:]...)
				flag = false
				count++
				break
			}
		}

		if flag {
			pair = append(pair, v)
		}
	}

	return count
}

// func main() {
// 	ar := []int32{10, 20, 20, 10, 10, 30, 50, 10, 20}
// 	var n int32
// 	n = 9
// 	sockMerchant(n, ar)
// }
