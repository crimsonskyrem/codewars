package main

import (
	"math"
)

func Code(s string) string {
	// your code
	var res string
	l := int(math.Sqrt(float64(len(s))))
	for i, c := range s {
		if i%l == 0 {
			res += string("\n")
		}
		res += string(c)
	}
	res += string(11)
	return res
}
func Decode(s string) string {
	// your code
	return ""
}

// func main() {
// 	d := "I.was.going.fishing.that.morning.at.ten.o'clock"
// 	// s := "c.nhsoI\nltiahi.\noentinw\ncng.nga\nk..mg.s\n\voao.f.\n\v'trtig"

// 	// fmt.Println(s)
// 	// d := "Process terminated with status 0 (0 minute(s), 6 second(s))"
// 	// s := "s t setP\n)se(tder\n)e(0a ro\n\vcs twmc\n\vo)muiie\n\vn,istns\n\vd n has\n\v(6u0 t "
// 	fmt.Println(Code(d))
// 	// fmt.Println(Decode(s))
// }
