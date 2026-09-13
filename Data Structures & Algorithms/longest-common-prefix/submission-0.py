class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        news=[]
        for ch  in zip(*strs):
            if len(set(ch))==1:
                news.append(ch[0])
            else:
                break
        return ''.join(news)



        

        
        