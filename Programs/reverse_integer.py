class Solution:
    def reverse(self, x: int) -> int:
        tw = 2**31
        if x < 0:
            return 0 if -int(str(-x)[::-1])<-tw else -int(str(-x)[::-1])
        else:
            return 0 if tw-1< int(str(x)[::-1]) else int(str(x)[::-1])