class Solution:
    def hIndex(self, citations: List[int]) -> int:
        ans = 0
        citations.sort(reverse = True)
        
        for index, value in enumerate(citations):
            if value > index:
                ans = index + 1
            
        return ans