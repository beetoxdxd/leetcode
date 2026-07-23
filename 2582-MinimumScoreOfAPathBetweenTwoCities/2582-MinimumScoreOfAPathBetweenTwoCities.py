# Last updated: 22/7/2026, 11:35:57 p.m.
class DSU:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.minimum = [math.inf] * size
        self.rank = [1] * size
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])  # Path Compression
        return self.parent[x]
    
    def union(self, x, y, dist):
        rootX = self.find(x)
        rootY = self.find(y)
        self.minimum[rootY] = min(dist, self.minimum[rootX], self.minimum[rootY])

        if rootX != rootY:
            self.parent[rootX] = rootY
        
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        nodes = DSU(n)

        for a, b, distance in roads:
            nodes.union(a-1, b-1, distance) 

        root = nodes.find(0)
        return nodes.minimum[root]