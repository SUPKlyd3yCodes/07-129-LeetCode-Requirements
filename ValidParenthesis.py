class Solution:
    def isValid(self, s: str) -> bool:
        p = []
        pdict = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for i in s:
            if p and i in pdict and pdict[i] == p[-1]:
                p.pop()
            else:
               p.append(i)
        return True if not p else False
            
            
