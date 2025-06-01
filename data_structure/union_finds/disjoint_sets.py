"""
A Python implementation of the Union-Find (Disjoint Set Union, DSU) data structure
with path compression and union by rank optimizations.

This structure is used to efficiently perform union and find operations on disjoint sets,
commonly applied in Kruskal’s algorithm, network connectivity, and dynamic connectivity problems.

Key Features:
- Path compression: Flattens the tree to speed up future find operations.
- Union by rank: Minimizes tree height by always attaching the smaller tree to the root of the larger one.
- Amortized nearly constant time complexity per operation: O(α(n)), where α is the inverse Ackermann function.     
"""


from typing import Dict

class UnionFind:    
    """Disjoint Set Union-Find data structure 
    with path compression and union by rank."""
    
    def __init__(self, n: int) -> None:
        """
        Initializes the disjoint set structure.
        """
        self.parent: Dict[int, int] = {}
        self.rank: Dict[int, int]   = {}

        self.make_set(n)

    def make_set(self, n: int)->None:
        """
        Creates n disjoint sets for elements 1 through n.
        """
        for i in range(1, n+1):
            self.parent[i] = i
            self.rank[i] = 0
    
    def findSet(self, u):
        """
        Find the representive (root) of the set that contains u
        Apply path compression for optimization
        ==> we can reduce the amount of these steps by by traversing
        up two vertices at the a time instead of one
        
        That would mean that when we are going up the tree, we can set
        """
        p = self.parent[u]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p

    def union(self, n1, n2):
        """
        Uses union by rank for optimization
        Returns:
            True if the sets were separate and were merged
            False if they were already in the same set
        """
        p1, p2 = self.findSet(n1), self.findSet(n2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
        elif self.rank[p2] < self.rank[p1]:
            self.parent[p1] = p2
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1
        
        return True
    


    def __str__(self) -> str:
        """
        Return a human-readable string representing the structure
        Element | Parent | Rank
        ------------------------
        1    |   2    |  0  
        2    |   4    |  1  
        3    |   4    |  0  
        4    |   4    |  2  
        5    |   5    |  0  
        """
        lines = ["Element | Parent | Rank", "------------------------"]
        for i in sorted(self.parent.keys()):
            lines.append(f"{i:^7} | {self.parent[i]:^6} | {self.rank[i]:^4}")
        return "\n".join(lines)
    
if __name__ == '__main__':
    uf = UnionFind(5)
    uf.union(1, 2)
    uf.union(3, 4)
    uf.union(2, 3)

    print(uf) 