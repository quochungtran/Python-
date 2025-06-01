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
    

import unittest
class TestUnionFind(unittest.TestCase):
    def setUp(self):
        self.uf = UnionFind(5)

    def test_initial_sets(self):
        for i in range(1, 6):
            self.assertEqual(self.uf.findSet(i), i)

    def test_union_and_find(self):
        self.assertTrue(self.uf.union(1, 2))
        self.assertEqual(self.uf.findSet(1), self.uf.findSet(2))

        self.assertTrue(self.uf.union(3, 4))
        self.assertEqual(self.uf.findSet(3), self.uf.findSet(4))

        self.assertTrue(self.uf.union(2, 3))
        self.assertEqual(self.uf.findSet(1), self.uf.findSet(4))

    def test_union_idempotence(self):
        self.uf.union(1, 2)
        self.assertFalse(self.uf.union(1, 2))  # already connected

    def test_transitive_connection(self):
        self.uf.union(1, 2)
        self.uf.union(2, 3)
        self.assertEqual(self.uf.findSet(1), self.uf.findSet(3))

if __name__ == '__main__':
    unittest.main()