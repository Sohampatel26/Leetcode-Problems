class Solution(object):
    def carFleet(self, target, position, speed):

        pair=[[p,s] for p,s in zip(position,speed)]
        pair.sort(reverse=True)

        lis=[]
        for p,s in pair:
            t=(float)(target-p)/s

            if lis and lis[-1]>=t:
                continue
            lis.append(t)

        return len(lis)
        



        
