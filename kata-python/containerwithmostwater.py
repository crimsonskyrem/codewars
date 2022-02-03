def maxArea( height ):
        lidx,ridx = 0 , len(height) - 1
        res = 0
        while lidx != ridx:
            if height[lidx] > height[ridx]:
                area = height[ridx] * (ridx - lidx)
                ridx -= 1
            else:
                area = height[lidx] * (ridx - lidx)
                lidx += 1
            res = max(res,area)
        return res

def test():
    assert maxArea( [1,8,6,2,5,4,8,3,7] ) == 49