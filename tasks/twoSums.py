class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
       # temp = {}
       # for item in nums:
       #     print(temp)
       #     if item not in temp:
       #         temp[target - item] = nums.index(item)
       #     else:
       #         if item == (target - item):
       #             nums.remove(item)
       #             return [temp[item],nums.index(item)+1]
       #         return [temp[item],nums.index(item)]
        temp={}
        for i in range(len(nums)):
            if nums[i] not in temp:
                temp[target - nums[i]] = i
            else:
                return [temp[nums[i]],i]
        

instance = Solution()
print("Trying with Array: [2,7,11,15]:")
result =  instance.twoSum([2,7,11,15],9)
print (result)
print("Trying with Array: [3,3]:")
result = instance.twoSum([3,3],6)
print (result)

