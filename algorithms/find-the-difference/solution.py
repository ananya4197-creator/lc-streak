from collections import Counter

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        a = Counter(nums)
        
        for num in sorted(a.keys(), reverse=True):
            if k <= a[num]:
                return num
            k -= a[num]