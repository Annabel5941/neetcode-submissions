class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #numbers is sorted in (not strictly) increasing order
        left = 0
        right = len(numbers) -1

        val = numbers[left] + numbers[right]

        while val != target:
            if val > target: #reduce value: decrease right pointer
                right -= 1
            else: #increase value: increase left value:
                left += 1

            val = numbers[left] + numbers[right]

        return [left+1, right+1]
        