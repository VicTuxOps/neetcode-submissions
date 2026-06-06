class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}
        visit = set()
        if not prerequisites:
            return True

        for course, pre in prerequisites:
            adjList[course].append(pre)
        
        for course in range(numCourses):
            print(course)
            if not self.dfs(course, adjList, visit):
                return False
        
        return True
        
    def dfs(self, course, adjList, visit):
        if course in visit:
            return False
        if adjList[course] == []:
            return True
            
        visit.add(course)
        for pair in adjList[course]:
            if not self.dfs(pair, adjList, visit):
                return False
        visit.remove(course)
        adjList[course] = []
        
        return True