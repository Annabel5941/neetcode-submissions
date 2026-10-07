from collections import Counter

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counter = Counter(nums)

        for item in counter:
            if counter[item] > 1:
                return True

        return False

        