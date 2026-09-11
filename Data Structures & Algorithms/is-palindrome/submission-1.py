class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = "".join(s.lower())
        news = ""
        for ch in s1:
            if ch.isalnum(): 
                news += ch

        n = len(news)
        li = -1  
        for fi in range(n // 2):
            if news[fi] == news[li]:
                li -= 1
            else:
                return False  
               
        return True 