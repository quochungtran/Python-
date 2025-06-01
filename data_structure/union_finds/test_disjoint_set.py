import unittest
from disjoint_sets import UnionFind

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