class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
        #for i in range(len(nums)):
            #for j in range(i+1 , len(nums)):
                #if nums[i] == nums[j]:
                    #return True
        #return False

        