class Solution:
    def longestPalindrome(self, s: str) -> str:
    
        if len(s) <= 1:
            return s 

        answer = ""
        new_s = s
        answer = [[0] * 100] * 1
        k = 0

        for i in range(0,len(new_s)):
            for strip in range(0,len(new_s)-i):
                if new_s[i:i+strip+1] == new_s[i:i+strip+1][::-1]: 
                    answer[0][k] = new_s[i:i+strip+1]
                    k = k+1

        length_z = 0        
        for i in range(0,k-1):
            length = len(answer[0][i])
            if (length > length_z):
                length_z = length
                answer_z = answer[0][i]
                
        return answer_z
#        a = 1

        
 #           while i - strip >= 0 and i < len(new_s) and new_s[i-strip:i+strip+1] == new_s[i-strip:i+strip+1][::-1]:

  #              answer = new_s[i-strip:i+strip+1]
  #              strip+=1
                
      #  a = ""
       # for i in answer:
       #     if i != '#':
       #         a+=i


  #      return a

l1 = 'babad'
sol = Solution()
result = sol.longestPalindrome(l1)