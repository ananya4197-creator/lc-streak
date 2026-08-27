class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtracking(s,open,close):
            if len(s) == 2*n:
                res.append(s)
                return

            if open <n:
                backtracking(s + "(", open +1,close)

            if close <open:
                backtracking(s + ")", open,close +1)

        backtracking("", 0,0)
        return res