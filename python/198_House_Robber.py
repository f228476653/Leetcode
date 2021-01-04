
class Solution:
    # temp1 failed
    # def rob(self, nums: List[int]) -> int:
    #     a = 0
    #     b = 0
    #     for i in range(len(nums)):
    #         if i%2 ==0 :
    #             a +=nums[i]
    #         else:
    #             b +=nums[i]
    #     return a if a>b else b

    def rob(self, nums) -> int:
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        dp = [0 for i in range(len(nums))] 
        dp[0] = nums[0]
        dp[1] = max(nums[0] , nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2]+nums[i] , dp[i-1])
        return dp[-1]
s = Solution()
m = s.rob([1,2,3,1])