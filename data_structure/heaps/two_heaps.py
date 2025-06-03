"""
Two Heaps
"""

import heapq

class Median:
    def __init__(self):
        self.small = []
        self.large = []
    
    def insert(self, inum):
        """
        Complexity : O(logN)
        """
        
        # push to max heap and swap with min heap if needed
        heapq.heappush(self.small, -1 * inum)
        if (self.small and self.large and (-1 * self.small[0] > self.large[0])):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        # handle uneven size
        if len(self.small) > len(self.large) + 1:
            val = -1  * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)

    
    def getMedian(self):
        """
        Complexity: O(N)
        """
        if len(self.small) > len(self.large) :
            return -1 * self.small[0]

        if len(self.large) > len(self.small):
            return self.large[0]

        return self.large[0] + (-1 * self.small[0]) // 2