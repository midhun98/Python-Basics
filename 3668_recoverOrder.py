class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friends = set(friends)
        res = []
        for x in order:
            if x in friends:
                res.append(x)
        return res