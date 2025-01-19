class Solution(object):
    def searchMatrix(self, matrix, target):
        m=len(matrix)
        n=len(matrix[0]) 

        top=0
        bot=m-1

        while top<=bot:
            cr=(top+bot)//2
            if target>matrix[cr][-1]:
                top=cr+1
            
            elif target<matrix[cr][0]:
                bot=cr-1
            
            else:
                break
            
        l=0
        r=n-1

        while l<=r:
            mi=(l+r)//2
            if target>matrix[cr][mi]:
                l=mi+1
            elif target<matrix[cr][mi]:
                r=mi-1
            else:
                return True
        
        return False
            

            
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        