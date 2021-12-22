package main

func VertMirror(s string) string {
	// your code
	return "vertmirror"
}
func HorMirror(s string) string {
	// your code
	return "hormirror"
}
type FParam func(string) string
func Oper(f FParam, x string) string {
	// your code
	return FParam(x)
}

func main() {
	s = "abcd\nefgh\nijkl\nmnop"

	// "dcba\nhgfe\nlkji\nponm"
	println(oper(vert_mirror, s))


	// "mnop\nijkl\nefgh\nabcd"
	println(oper(hor_mirror, s))
}
