class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result=[]
        while matrix:
            result += matrix.pop(0)
        
            if matrix:
                matrix = list(zip(*matrix))[::-1]
        return result

        