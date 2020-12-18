
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0
        max_len ,length_r, length_l,length=0,0,0,0
        goDown =False
        for i in range(1,len(A)):
            #print("int i",A[i])
            if goDown:
                if (A[i-1] > A[i]):
                    length_l+=1
                    #print("3",length_l)
                else:
                    length = min(length_l,length_r)
                    max_len = max(2*length+1,max_len)
                    #print("4",length)
                    #print("4",max_len)
                    length_l=0
                    length_r=0
                    goDown =False
            if not goDown:
                if(A[i-1] > A[i]):
                    goDown =True
                    length_l+=1
                    #print("2")
                if A[i-1] < A[i]:
                    length_r+=1
                    goDown =False
                    #print("1",length_r)
        print(length_l)
        print(length_r)
        if(length_l>0 and length_r>0):
            length = min(length_l,length_r)
            max_len = max(length*2+1,max_len)
        if max_len<3:max_len=0
        return max_len