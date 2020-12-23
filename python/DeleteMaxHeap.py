
class Solution:
    def deleteMaxHeap(self, a,i):
        a[i] = a[len(a)-1]
        a= a[0:-1]
        print(a)
        return self.sort(a,i)

    def sort(self, a,i):
        parent = (i-1)//2
        print(parent)
        if a[parent] < a[i]:
            temp = a[parent] 
            a[parent] =a[i]
            a[i] =temp
        return a



        
            
            
        


if  __name__ == "__main__":
    re=Solution().deleteMaxHeap([15,7,9,1,2,3,8],4)
    print(re)
        
        