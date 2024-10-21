class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        x1, y1 = coordinate1[0], coordinate1[1]
        x2, y2 = coordinate2[0], coordinate2[1]

        x1 = ord(x1) - 96
        x2 = ord(x2) - 96
        data = {"oddodd": False, "oddeven": True, "evenodd": True, "eveneven": False}
        out1 = ""
        out2 = ""
        if (int(x1) % 2) == 0:
            out1 += "even"
        else:
            out1 += "odd"
        if (int(y1) % 2) == 0:
            out1 += "even"
        else:
            out1 += "odd"

        if (int(x2) % 2) == 0:
            out2 += "even"
        else:
            out2 += "odd"
        if (int(y2) % 2) == 0:
            out2 += "even"
        else:
            out2 += "odd"

        return data[out1] == data[out2]


ss = Solution()
coordinate1 = "a1"
coordinate2 = "c3"
print(ss.checkTwoChessboards(coordinate1, coordinate2))
