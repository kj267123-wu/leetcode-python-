class Solution:
    def longestPalindrome(self, s: str) -> str:
    
        if len(s) <= 1:
            return s 

        answer = ""
        new_s = "#"
        for i in s:
            new_s +=i + "#"

        strip = 1
        

        for i in range(1,len(new_s)-2):
                      
            while i - strip >= 0 and i + strip < len(new_s) and new_s[i-strip:i+strip+1] == new_s[i-strip:i+strip+1][::-1]:

                answer = new_s[i-strip:i+strip+1]
                strip+=1
                
        a = ""
        for i in answer:
            if i != '#':
                a+=i

        return a

l1 = 'babad'
sol = Solution()
result = sol.longestPalindrome(l1)