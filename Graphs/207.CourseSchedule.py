from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # 这个题的核心思路就是找directed graph里有没有cycle
    adj = [[] for _ in range(numCourses)]
    for prerequisite in prerequisites:
        adj[prerequisite[1]].append(prerequisite[0])
    # 用adj表示这个directed graph

    visited = [False for _ in range(numCourses)]
    # visited表示当前node是否被访问过
    instack = [False for _ in range(numCourses)]
    # instack表示在这个directed graph里，这个node是不是在当前路径里
    # 如果instack[node]为true，那表示这条路径正在走而且又回到之前的node了，所以有cycle

    def dfs(node, adj, visited, instack):
        if instack[node]:
            return True
        # 如果在遍历邻居的时候，发现一个“已经在当前递归路径中的节点”，就说明图中有cycle
        if visited[node]:
            return False
        # 如果

        visited[node] = True
        # 这个node访问过了
        instack[node] = True
        # 这个路径节点访问过了
        for neighbor in adj[node]:
            if dfs(neighbor, adj, visited, instack):
                # 如果这个dfs return true，表示有cycle
                return True
        instack[node] = False
        # 这个路径访问完了，为了防止之后误判cycle，要把这个路径的stack改为false
        return False

    for i in range(numCourses):
        if dfs(i, adj, visited, instack):
            return False
    return True


print(canFinish(2, [[1, 0]]))
