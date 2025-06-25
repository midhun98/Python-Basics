from typing import List


class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        out = []
        for li in image:
            li.reverse()
            out.append([val ^ 1 for val in li])
        return out


ss = Solution()
image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
print(ss.flipAndInvertImage(image))
