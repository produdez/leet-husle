class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
            Version 2.5: Update more optimize code
            - Prefix (left) Suffix(right) -> prodExceptSelf (left * right)
            - Ilteratively calculate cumulative muttiplication prefix and suffix
            - And update the result in result array
            
            Complexity: Much better
            Time: O(~2n) -> O(n) (similar to version 2)
            Space: O(n) (3 times better than version 2)
            Extra-note: problem stated that output array does not count in space
            complexity -> so it's technically O(1)
        '''
        result = [1] * len(nums)
        
        prefix = 1
        postfix = 1
        for i in range(len(nums)):
            result[i] *= prefix
            prefix *= nums[i]
            
            result[len(nums)-1 -i] *= postfix
            postfix *= nums[len(nums)-1 -i]
        
        return result