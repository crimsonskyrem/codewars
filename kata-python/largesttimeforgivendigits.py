def largestTimeFromDigits(arr) -> str:
    length = len(arr)
    result = []
    enumArr(sorted(arr, reverse=True),[],[False]* length, result)
    for i in range(len(result)):
        res = result[i]
        if (res[0] * 10 + res[1]) < 24 and res[2] < 6:
            return "{}{}:{}{}".format(res[0],res[1],res[2],res[3])
    return ""

def enumArr(input_arr, form_arr, used ,all_arr):
    if all(x for x in used):
        all_arr.append(form_arr)
    for i in range(len(input_arr)):
        if used[i] == False:
            new_form = form_arr.copy()
            new_form.append(input_arr[i])
            new_used = used.copy()
            new_used[i] = True
            enumArr(input_arr, new_form, new_used, all_arr)

print(largestTimeFromDigits([1,2,3,4]) == "23:41")
print(largestTimeFromDigits([5,5,5,5]) == "")
