from typing import List
from collections import Counter


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        data_dict = dict(Counter(arr))
        out = []
        for key, value in data_dict.items():
            if value == 1:
                out.append(key)

        k = k - 1
        try:
            return out[k]
        except:
            return ""


ss = Solution()
arr = ["aaa", "aa", "a"]
k = 2
print(ss.kthDistinct(arr, k))
