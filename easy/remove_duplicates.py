class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = []
        for num in nums:
            if num not in seen:
                seen.append(num)
        nums[:len(seen)] = seen
        return (len(seen))