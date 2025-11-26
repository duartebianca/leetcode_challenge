class Solution:
    def pivotInteger(self, n: int) -> int:
        limite = n+1
        for i in range(1, limite):
            if (sum(range(1, i+1)) == sum(range(i, limite))):
                return i
        return -1
 
        
