class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        seen = []
        for num in nums:
            if num != val:
                seen.append(num)
        nums[:len(seen)] = seen
        return (len(seen))
        
        