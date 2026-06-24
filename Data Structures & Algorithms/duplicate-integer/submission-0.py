class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_table = {}
        for key in nums:
            if key in hash_table:
                return True
            else:
                hash_table[key] = 1
        return False
        

         