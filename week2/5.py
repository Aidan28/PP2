from functools import reduce 
class Solution: 
    def subtractProductAndSum(self, n: int) -> int:
        digits = [int(i) for i in str(n)]
        return reduce ((lambda x,y:x*y), digits)- sum(digits)
    