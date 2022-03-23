def longestCommonPrefix(strs) -> str:
    if len(strs) == 0:
        return ''
    length = min(map(len, strs))
    if length == 0:
        return ''
    pos = 0
    while pos < length:
        for i in range(1, len(strs)):
            if strs[i][pos] != strs[0][pos]:
                return strs[0][:pos]
        pos += 1
    return strs[0][:pos]

print(longestCommonPrefix(["flower", "flow", "flight"]) == "fl")
print(longestCommonPrefix(["dog","racecar","car"]) == "")
print(longestCommonPrefix(["cir","car"]) == "c")