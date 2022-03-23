def longestCommonPrefix(strs) -> str:
    if len(strs) == 0:
        return ''
    length = min(map(len, strs))
    if length == 0:
        return ''
    match = [False] * length
    pos = 0
    while pos < length:
        for i in range(1, len(strs)):
            if strs[i][pos] != strs[0][pos]:
                return ''.join(map(lambda x: x[0] if x[1] else '', zip(strs[0], match)))
        match[pos] = True
        pos += 1
    return ''.join(map(lambda x: x[0] if x[1] else '', zip(strs[0], match)))


print(longestCommonPrefix(["flower", "flow", "flight"]) == "fl")
print(longestCommonPrefix(["dog","racecar","car"]) == "")
print(longestCommonPrefix(["cir","car"]) == "c")