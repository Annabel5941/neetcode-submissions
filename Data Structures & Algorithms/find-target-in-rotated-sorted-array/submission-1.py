class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low+high)//2

            if nums[mid] == target:
                return mid

            #left side is sorted
            if nums[low] <= nums[mid]:
                #target is in this half
                if nums[low] <= target < nums[mid]:
                    high = mid-1 

                #not in this half; search right next
                else:
                    low = mid+1

            #right side is sorted
            else:
                #target is in this half
                if nums[mid] < target <= nums[high]:
                    low = mid+1
                
                #not in this half; search left next
                else:
                    high = mid-1


        return -1
        