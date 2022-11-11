class Solution:
    def reverse(self, x: int) -> int:
        
        s = str(x)
        i = len(s)-1
        temp = []
        
        if s[0] == '-':
            temp.append(s[0])
        
        while i >= 0:
            if s[i]== '-':
                i -= 1
            else:
                temp.append(s[i])
                print(temp)
                i -= 1
            
        temp_string = "".join(temp)
        print(temp_string)
            
        x = int(temp_string)
        
        if x > 2**31 - 1:
            return 0
        elif x < -2**31:
            return 0
        else:
            return x