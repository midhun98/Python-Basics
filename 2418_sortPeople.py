from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_dict = {}        
        for index, value in enumerate(heights):
            height_dict[value] = index
            
        myKeys = heights
        myKeys.sort()
        sorted_dict = {}

        for i in myKeys:
            sorted_dict[i] = height_dict[i]

        out = []
        for key, value in sorted_dict.items():
            out.append(names[value])
        return out[::-1]


ss = Solution()
names = ["Mary","John","Emma"]
heights = [180,165,170]
print(ss.sortPeople(names, heights))