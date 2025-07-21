from typing import List


def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    adj = [[] for _ in range(numCourses)]
    for prerequisite in prerequisites:
        adj[prerequisite[1]].append(prerequisite[0])
    visited = [False for _ in range(numCourses)]
    instack = [False for _ in range(numCourses)]
    ans = []

    def dfs(node, adj, visited, instack, ans):
        if instack[node]:
            return True
        if visited[node]:
            return False

        visited[node] = True
        instack[node] = True

        for neighbor in adj[node]:
            if dfs(neighbor, adj, visited, instack, ans):
                return True
        instack[node] = False

        # 前面的逻辑跟207题是一样的，然后在当前路径跑完之后再把这个node存起来(postorder)
        ans.append(node)
        return False

    for i in range(numCourses):
        if dfs(i, adj, visited, instack, ans):
            return []

    return ans[::-1]


print(findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
