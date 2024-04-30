ans = 0
def solution(n, computers):
    global ans
    
    visited = [0 for i in range(n)]
    
    for i in range(n):
        if visited[i] == 0:
            dfs(n, computers, i, visited)
            ans += 1
        
    return ans

def dfs(n, computers, i, visited):
    visited[i] = 1
    
    for j in range(n):
        if i != j and computers[i][j] == 1:
            if visited[j] == 0:
                dfs(n, computers, j, visited)