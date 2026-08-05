class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        map=dict()
        map[0]=1
        prefixsum=0
        count=0
        for i in range(len(nums)):
            prefixsum+=nums[i]
            target=prefixsum % k

            if target in map:
                count+=map.get(target)

            map[target]=map.get(target,0)+1
            
        return count

