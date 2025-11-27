class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        expected = []
        for number in range (0, len(nums)+1):
            expected.append(number)
        diff = list(set(expected) - set(nums))
        return diff[0]