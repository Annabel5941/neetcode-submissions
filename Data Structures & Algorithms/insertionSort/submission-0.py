# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        output = []

        #iterate through each index in turn
        for i in range(len(pairs)):
            #if bigger than the previous item, swap... go through each previous item in turn
            for j in range(i-1, -1, -1):
                if pairs[j].key > pairs[j+1].key:
                    pairs[j], pairs[j+1] = pairs[j+1], pairs[j]
                else:
                    break

            output.append(pairs.copy())
        
        return output