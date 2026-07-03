class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero = 0
        for num in nums:
            if num != 0:
                total *= num
            else:
                zero += 1 
        
        output = []
        
        for i, num in enumerate(nums):
            if zero == 0:
                output.append(int(total/num))
            elif zero == 1:
                if num != 0:
                    output.append(0)
                else: 
                    output.append(total)
            elif zero > 1:
                output.append(0)

        return output