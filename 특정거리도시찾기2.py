from collections import deque
import time

INF = int(1e9)

n, m, k, x = map(int, input().split())
start = time.time()

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] =0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

#print(graph)

for kk in range(1, n + 1):
    for aa in range(1, n + 1):
        for bb in range(1, n + 1):
            graph[aa][bb] = min(graph[aa][bb], graph[aa][kk] + graph[kk][bb])

#print(graph)

check =0 
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == 2:
            print(b)
            check += 1
        
            
if check ==0 :
     print("-1")

end = time.time()
print(end - start)
