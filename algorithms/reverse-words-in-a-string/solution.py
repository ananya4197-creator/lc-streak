class Solution:
    def reverse(self, x: int) -> int:
        y = str(x)
        
        if y[0] == "-":
            ans =   "-" + y[:0: -1]

        else:
            ans =   int(y[:: -1])
          
        ans = int(ans)

        if ans < -2**31 or ans >2**31 :
            return 0

        return ans
            