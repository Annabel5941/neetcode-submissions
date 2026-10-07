class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        #search!
        while high >= low:
            mid = (high+low)//2
            val = nums[mid]

            print(f"Index: {mid}, Value: {val}")
            if val == target:
                return mid

            elif val < target:
                low = mid+1
            
            else:
                high = mid-1

        return -1
        