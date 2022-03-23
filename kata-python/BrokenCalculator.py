class Solution:
    # If X > Y, we do not have a lot of choice, we can just decrease X by one until it becomes equal to Y, so answer will be X - Y.
    # If X == Y, then we already happy and we return 0.
    # If Y % 2 == 1, then let us think, what can be the last step? It can not be multilication by 2, so the only choice is subtraction of 1 and on previous step we have configuration (X, Y + 1), for which we run our function recursively.
    # If Y % 2 == 0, let us prove that we always need to divide by 2 in this case.

    def brokenCalc(self, X, Y):
        if X > Y: return X - Y
        if X == Y: return 0
        if Y % 2 == 0:
            return self.brokenCalc(X, Y//2) + 1
        else:
            return self.brokenCalc(X, Y + 1) + 1

s = Solution()
print(s.brokenCalc(2,3) == 2)
print(s.brokenCalc(5,8) == 2)
print(s.brokenCalc(3,10) == 3)