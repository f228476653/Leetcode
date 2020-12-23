
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rs = []
        temp ={}
        for s in strs:
            sort = sorted(s)
            key = "".join(sort)
            if temp.get(key):
                temp[key].append(s)
            else:
                temp[key]=[]
                temp[key].append(s)
        rs=list(temp.values())
        return rs   
            
            
        


if  __name__ == "__main__":
    a=Solution()
    re =a.groupAnagrams(["ser","res"])
        
        