class Solution:
    def diffWaysToCompute(self, expression):
        ans = []

        for i in range(len(expression)):
            if expression[i] in "+-*":
                
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])

                for a in left:
                    for b in right:
                        if expression[i] == "+":
                            ans.append(a + b)
                        elif expression[i] == "-":
                            ans.append(a - b)
                        else:
                            ans.append(a * b)

        if not ans:
            ans.append(int(expression))

        return ans