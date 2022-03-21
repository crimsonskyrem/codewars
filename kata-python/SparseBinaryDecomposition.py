from math import ceil, log2


def calculate_alternating_mask(value):
    """
    calculate_alternating_mask determines a binary mask with a maximum
    range based on the provided value, then iterates through each bit in
    the mask, alternating the setting of that bit to 0.

    the end result is a mask with at most every other bit set to 1, in the
    worst case scenario that all bits were 1 in the binary representation
    of the input value.

    @example: calculate_alternating_mask(15) -> 0b1010
    @example: calculate_alternating_mask(0b1111) -> 0b1010
    @example: calculate_alternating_mask(0xf) -> 0b1010

    @example: calculate_alternating_mask(255) -> 0b10101010
    @example: calculate_alternating_mask(0b11111111) -> 0b10101010
    @example: calculate_alternating_mask(0xff) -> 0b10101010
    """
    binary_index = ceil(log2(value))
    alternating_mask = 2 ** binary_index - 1

    zero_bit = 1
    while binary_index >= 0:
        if (zero_bit == 1):
            alternating_mask -= 2 ** binary_index

        zero_bit ^= 0b1
        binary_index -= 1

    return alternating_mask


def solution(N):
    """
    solution will specially handle cases at the minimum range of valid
    input values to return early. otherwise, an alternating mask will
    be generated to calculate a sparse integer based on the value.
    """
    if N <= 2:
        return N

    return N & calculate_alternating_mask(N)


# print(solution(26) in [5, 8, 9, 10, 16, 17, 18, 21])
print(solution(74901729))
# print(solution(216188401))
# print(solution(1000000000))
