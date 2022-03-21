def supers(number):
    zeros = sum(1 for bit in range(30) if (number >> bit) & 1 == 0)
    return 2**zeros


def solution(a,b,c):
    total = supers(a) + supers(b) + supers(c)
    total -= supers(a | b) # counted twice, remove one
    total -= supers(b | c) # counted twice, remove one
    total -= supers(a | c) # counted twice, remove one
    total += supers(a | b | c) # counted three times, removed three times, add one

    return total


print(solution(1073741727,1073741631,1073741679) == 8)
print(solution(0,0,0) == 1073741824)
print(solution(1073741823,1073741823,1073741823) == 1)

#Explanation
# Let S(n) be the set produce by the number n.
# supers(n) returns |S(n)| the size of the set for the number n. supers is not a great name, but I had trouble coming up with a better one
# The trick is to realize that S(a) ^ S(b) = S(a | b). As a result, using supers I can figure out the size of all those sets.
# To figure out the rest, draw a venn diagram of the sets. 