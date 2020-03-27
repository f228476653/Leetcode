class Solution(object):

    def twoSum(self, nums, target):
        # two point
        afterOrder = enumerate(nums)
        for index, value in afterOrder:
            secondNum = target - value
            if secondNum in nums[index+1:]:
                    return [index, nums.index(secondNum,index+1)]
        return None
    
    def twoSumTemp2(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining not in dict:
                dict[nums[i]] = i
            else:
                return [ dict[remaining], i]
        return None
        

if __name__ == '__main__':
    # begin
    s = Solution()
    print s.twoSum([3, 2, 4], 6)
    print s.twoSum([3, 3], 6)
