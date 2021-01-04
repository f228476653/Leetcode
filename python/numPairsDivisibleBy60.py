class Solution:
    # 太慢
    # def numPairsDivisibleBy60(self, time) -> int:
    #     rest =[]
    #     pair=0
    #     for i in time:
    #         restAfterMod =i%60
    #         find = 0
    #         if restAfterMod:
    #             find =60 -restAfterMod 
    #         for i in rest:
    #             if i== find:
    #                 pair+=1
    #         rest.append(restAfterMod)
    #     return pair

    def numPairsDivisibleBy60(self, time) -> int:
        rest =[0]*60
        pair=0
        for i in time:
            restAfterMod =i%60
            find = 0
            if restAfterMod:
                find =60 -restAfterMod 
            pair+=rest[find]
            rest[restAfterMod]+=1
        return pair


if __name__ == "__main__":
    s =Solution()
    rs =s.numPairsDivisibleBy60([60,60,60])
    print(rs)