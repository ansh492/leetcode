class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map=dict()
        for i in nums:
            map[i]=map.get(i,0) +1

        map = dict(sorted(map.items(), key=lambda item: item[1], reverse=True))

        res = []
        for key in map: 
            res.append(key)
            if len(res) == k:
                break

        return list(res)