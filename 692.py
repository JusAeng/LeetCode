class Solution:
    def topKFrequent(self, words: list, k: int) -> list:
        c = []
        for ele in sorted(list(set(words))):
            c.append([ele,words.count(ele)])
        c.sort(reverse=True,key= lambda s: s[1])
        print(c)
        return [x[0] for x in c[:k]] 