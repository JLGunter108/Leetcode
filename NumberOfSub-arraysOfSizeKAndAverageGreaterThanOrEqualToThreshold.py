class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        count = 0
        total = 0

        for i in range(0, k):
            total = total + arr[i]
        
        if total/k >= threshold:
                count+=1
        
        j = k
        
        while j < len(arr):
            total -= arr[j-k]
            total += arr[j]
            
            if total/k >= threshold:
                count+=1
            
            j+=1
            
        return count