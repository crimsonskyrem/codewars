def lengthOfLongestSubstring(s: str) -> int:
	arr = list(s)
	res = len(arr)
	res_l = res
	if res == 0:
		return res
	res = 0
	for i in range(res_l):
		tmp = [arr[i]]
		if i > (res_l/2) and i< res:
			return res
		for j in range(1,res_l - i):
			if arr[i+j] in tmp:
				if len(tmp) > res:
					res = len(tmp)
				break
			else:
				tmp.append(arr[i+j])
		if len(tmp) > res:
			res = len(tmp)
	return res
def lengthOfLongestSubstring2(s: str) -> int:
	l = len(s)
	if l < 2:
		return l
	start = 0
	res = 1
	tmp = {s[0]: 0}
	for i in range(1, l):
	# if char was seen before and if start of substring is before the char's previous index,
	# update substring to start from next char
		if s[i] in tmp and start <= tmp[s[i]]:
			start = tmp[s[i]] + 1
		tmp[s[i]] = i
		res = max(res, i - start + 1)
	return res


# print(lengthOfLongestSubstring('dvcdfc'))
print(lengthOfLongestSubstring2('dvcdfc'))