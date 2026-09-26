class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        
        dic = {}
        for key , value in knowledge:
            dic[key] = value

        result = ""
        i = 0
        
        while i < len(s):
            
            if s[i] == "(":
                i+= 1
                key = ""
                while s[i] != ")":
                    key  += s[i]
                    i+=1

                if key in dic:
                    result += dic[key]
                else:
                    result += "?"

                i += 1

            else:
                
                result += s[i]
                i += 1

        return result
                    
  