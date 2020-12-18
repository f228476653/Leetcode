class Solution:
    def dailyTemperatures(self, T):
        stack =[]
        ans=[0]*len(T)
        for i,t in reversed(list(enumerate(T))):
            while stack and stack[-1][1] <= t:
                stack.pop(len(stack)-1)
            if len(stack)>0:
                ans[i] = stack[-1][0]-i
            stack.append((i,t))
        return ans

if __name__ == "__main__":
    s = Solution()
    s.dailyTemperatures([73,74,75,71,69,72,76,73])
            

        