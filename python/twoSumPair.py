class Solution:
    def uniquePairs(self, nums, target):
        res = {}
        out = set()

        for index, value in enumerate(nums):
            print(f'{index} {value}')
            if target - value in res:
                out.add((value, target-value))
            else:
                res[value]=index

        return len(out)


if __name__ == "__main__":
    s =Solution()
    rs =s.uniquePairs([1,2,3,4,45,46],47)
    print(rs)