from typing import List


# If RIGHT: +1
# If LEFT: -1
# If DOWN: +n
# If UP: -n


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        out = 0
        for command in commands:
            if command == "RIGHT":
                out += 1
            if command == "LEFT":
                out -= 1
            if command == "DOWN":
                out += n
            if command == "UP":
                out -= n
        return out


ss = Solution()
n = 2
commands = ["DOWN", "RIGHT", "UP"]
print(ss.finalPositionOfSnake(n, commands))
