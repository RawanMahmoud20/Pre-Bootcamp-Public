class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        freq = {}
    # Count frequency of each character

        for char in s:
            if char in freq:
                freq[char]+=1
            else:
                freq[char]=1
    # Get all frequency values
    
        values=list(freq.values())              
    # Check if all frequencies are equal
        return len(set(values)) == 1  
    
    
# Create object from Solution class
sol=Solution()   

 # Test cases
print(sol.areOccurrencesEqual("abacbc"))  # Expected: True
print(sol.areOccurrencesEqual("aaabb"))   # Expected: False
print(sol.areOccurrencesEqual("a"))       # Expected: True
print(sol.areOccurrencesEqual("zzzz"))    # Expected: True
