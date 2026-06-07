class Graph:
    
    def __init__(self):
        self.val = 0
        self.neighbors = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.neighbors:
            self.neighbors[src] = set()
        if dst not in self.neighbors:
            self.neighbors[dst] = set()
        self.neighbors[src].add(dst)

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
            if dst in self.neighbors[src]:
                return True
            visit.add(src)
            flag = False
            for e in self.neighbors[src]:
                flag = dfs(e, dst, visit)
                if flag:
                    break
            return flag
        return dfs(src, dst, visit)
