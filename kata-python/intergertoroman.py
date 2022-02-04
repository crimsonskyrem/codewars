def intToRoman(num: int) -> str:
    if num > 999:
        return "M" * (num // 1000) + intToRoman(num % 1000)
    elif num > 99:
        return subIntToRoman(num,100,"C","D","M") + intToRoman(num % 100)
    elif num > 9:
        return subIntToRoman(num,10,"X","L","C") + intToRoman(num % 10)
    elif num > 0:
        return subIntToRoman(num,1,"I","V","X")
    else:
        return ""

def subIntToRoman(num,divisor,one,five,ten) :
    if num == 0:
        return ""
    if num < 4 * divisor:
        return one * (num // divisor)
    elif num < 5 * divisor:
        return one + five
    elif num < 6 * divisor:
        return five
    elif num < 9 * divisor:
        return five + one * (num // divisor -5)
    elif num < 10 * divisor:
        return one + ten

def test():
    assert intToRoman(1) == "I"
    assert intToRoman(3) == "III"
    assert intToRoman(4) == "IV"
    assert intToRoman(9) == "IX"
    assert intToRoman(58) == "LVIII"
    assert intToRoman(60) == "LX"
    assert intToRoman(1994) == "MCMXCIV"
