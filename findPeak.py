class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        while l<=h:
            mid=(l+h)//2
            if (mid==0 or nums[mid]>nums[mid-1]) and (mid==len(nums)-1 or nums[mid]>nums[mid+1]):
                return mid
            elif mid>0 and nums[mid]<nums[mid-1]:
                h=mid-1
            else:
                l=mid+1
        return -1
        
