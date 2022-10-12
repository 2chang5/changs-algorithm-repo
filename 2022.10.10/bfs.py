from collections import deque

graph = {}

graph['A'] = ["B","C"]
graph['B'] = ["A","D"]
graph['C'] = ["A","G","H","I"]
graph['D'] = ["B","E","F"]
graph['E'] = ["D"]
graph['F'] = ["D"]
graph['G'] = ["C"]
graph['H'] = ["C"]
graph['I'] = ["C","J"]
graph['J'] = ["I"]



#함수화 시켜서 쓸꺼
# 그래프는 graph,start_node는 시작점

# 강의에서는 queue 안쓰고 list 썻음 적절히 뜯어고쳐봐야지

def bfs (graph,start_node):
    visited = []
    need_visited= deque()

    #최초할일 need_visited에다가 start넣기
    need_visited.append(start_node)

    #while 문 조건으로 need_visited에 뭐가있는지없는지 이제 탐색할꼐 있는지 없는지 판단
    while need_visited:
        # 임시저장소 node에 가장 왼쪽 원소 뽑아서 visited에 있나 판단후 없다면 append하면서 need_visited 에도 원소 추가 
        node = need_visited.popleft()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])

    return visited


print(bfs(graph=graph,start_node="A"))

# 구현은 간단하다