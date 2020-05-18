package main

func RemovNb(m uint64) [][2]uint64 {
	res := [][2]uint64{}
	sum := (m*m + m) / 2

	for i := m / 2; i < m; i++ {
		j := (sum - i) / (i + 1)
		if sum-i-j == i*j {
			res = append(res, [2]uint64{i, j})
		}
	}
	if len(res) < 1 {
		return nil
	}
	return res
}

// func main() {
// 	// res := RemovNb(26)
// 	res := RemovNb(1000003)
// 	fmt.Println(res)
// }
