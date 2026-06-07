class Graph:
    
    def __init__(self):
        self.neighbors = defaultdict(set)

    def addEdge(self, src: int, dst: int) -> None:
        self.neighbors[src].add(dst)
        self.neighbors[dst]

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.neighbors and dst in self.neighbors[src]:
            self.neighbors[src].remove(dst)
            return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        visit = set()
        def dfs(src, dst, visit):
            if src == dst:
                return True
            if src in visit:
                return False
            if src in self.neighbors and dst in self.neighbors[src]:
                return True
            visit.add(src)
            for e in self.neighbors.get(src, set()):
                if dfs(e, dst, visit):
                    return True
            return False
        return dfs(src, dst, visit)
