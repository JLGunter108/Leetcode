class Solution:
    def maxArea(self, height: List[int]) -> int:
        volume = 0
        l, r = 0, len(height)-1
        
        while l != r:
            if height[l] < height[r]:
                if height[l]*(r-l) > volume:
                    volume = height[l]*(r-l)
                    l+=1
                else:
                    l+=1
            elif height[l] > height[r]:
                if height[r]*(r-l) > volume:
                    volume = height[r]*(r-l)
                    r-=1
                else:
                    r-=1
            else:
                if height[l]*(r-l) > volume:
                    volume = height[l]*(r-l)
                    l+=1
                else:
                    l+=1
                    
        return volume