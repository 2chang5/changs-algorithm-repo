# BFS 랑 구현방식 같은건 알겠는데 어쩃든 문제는 재귀로 풀어야할텐데 그건왜 안나와

from collections import deque

def dfs(graph,start_node):
    visited = list()
    need_visited = deque() #스택 정책이용

    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])


#재귀찾아서 떠나보자

# python
def dfs(graph, v, visited):
  # 현재 노드를 방문처리
  visited[v]=True
  print(v,end=' ')
  # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)