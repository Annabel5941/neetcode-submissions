import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)

        prod = math.prod(nums)

        for i in range(len(output)):
            if nums[i] != 0:
                output[i] = int(prod/nums[i])
            else:
                output[i] = int( math.prod(nums[:i])*math.prod(nums[i+1:]) )

        return output
        