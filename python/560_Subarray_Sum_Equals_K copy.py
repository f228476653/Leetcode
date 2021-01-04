# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         rs = 0
#         for i in range(len(nums)):
#             target = k
#             for n in range(i,len(nums)):
#                 target=target-nums[n]
#                 if target==0 :
#                     rs+=1
#         return rs
class Solution:
    def subarraySum(self, nums, k: int) -> int:
        cur_sum=0
        rs=0
        mapData = {0:1}
        for num in nums:
            cur_sum += num
            print(f'cur_sum {cur_sum}')
            print(f'cur_sum-k {cur_sum-k}')
            print(f'get {mapData.get(cur_sum)}')
            if mapData.get(cur_sum-k):
                rs +=mapData.get(cur_sum-k)
            if mapData.get(cur_sum):
                mapData[cur_sum] += 1
            else:
                mapData[cur_sum] = 1
        return rs


if  __name__ == "__main__":
    a=Solution()
    re =a.subarraySum([1,-1,0],0)
    print(re)
        
        