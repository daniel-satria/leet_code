from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for x in nums:
            if abs(x) < abs(closest):
                closest = x
        
        if closest < 0 and abs(closest) in nums:
            print(abs(closest))
            return abs(closest)
        else:
            print(closest)
            return closest
        

angka = [2, 21, -2, 3]

Solution().findClosestNumber(angka)