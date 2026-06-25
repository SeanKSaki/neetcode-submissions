class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = - 1
        for num in nums:
            if count < 0:
                candidate = num
            count += 1 if candidate == num else -1
        return candidate