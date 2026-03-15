class Solution:
    def countPairs(self, words: List[str]) -> int:
        # diff

        def countDoff(c1,c2):
            c1Num = ord(c1) - ord('a')
            c2Num = ord(c2) - ord('a')
            if c2Num > c1Num:
                return c2Num - c1Num
            else:
                return c2Num + 26 - c1Num

        transDisc = defaultdict(list)
        for i in range(len(words)):
            curWord = words[i]
            if len(curWord) == 1:
                transDisc[i].append(0)
            else:
                for j in range(1,len(curWord)):
                    transDisc[i].append(countDoff(curWord[j-1],curWord[j]))
        # print(transDisc)
        pairMap =  defaultdict(int)
        res = 0
        for key,val in transDisc.items():
            # print(val)
            res+= pairMap[tuple(val)]
            pairMap[tuple(val)] += 1
        return res


        