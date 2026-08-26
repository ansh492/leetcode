class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr=[]
        zero_count=nums.count(0)
        if zero_count>1:
            return [0]*len(nums)
        if zero_count==1:
            pro=1
            for i in nums:
                if i!=0:
                    pro*=i
                if i==0:
                    continue

            for j in nums:
                if j!=0:
                    arr.append(0)
                else:
                    a=pro
                    arr.append(a)

        if zero_count==0:
            pro=1
            for i in nums:
                pro*=i
            for j in nums:
                arr.append(pro//j)
        return arr