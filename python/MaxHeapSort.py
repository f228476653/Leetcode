
class Solution:
    def maxHeapSort(self, a):
        rs = [None] * len(a)
        j=0
        while len(a)>0:
            for i in range(len(a)-1,0,-1):
                #print(i)
                if a[i]>a[0]: #a[i] 與 root交換
                    temp=a[i]
                    a[i]=a[0]
                    a[0]=temp
            rs[j]= a[0]
            j+=1
            a= a[1:] #root是最大的了 所以去掉
        return rs   
            
            
        


if  __name__ == "__main__":
    re=Solution().maxHeapSort([5,3,17,10,84,19,6,22,9])
    print(re)
        
        