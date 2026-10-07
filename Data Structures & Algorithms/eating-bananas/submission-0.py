import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles) #max is the largest value - can't be faster than eating each pile one at a time in the hour

        #binary search...
        #need k to be true, k-1  to be false (otherwise we could lower k)
        #so, if it is true, try increasing, false, try decreasing...

        while low <= high:
            mid = (low+high)//2
            #value is the sum of each of the piles, ceil(/k)
            val = sum(math.ceil(pile/mid) for pile in piles)

            

            #update values
            if val <= h:
                res = mid #record if valid!
                #try something smaller
                high = mid-1

            else:
                #try something bigger
                low = mid+1

        return res

        