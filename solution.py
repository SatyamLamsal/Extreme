import sys

data = sys.stdin.read().splitlines()

n, m = map(int, data[0].strip().split())

grid = [list(data[i+1]) for i in range(n)]


# print(grid)



parent = list(range(n*m))
digit = [0] * (n*m)

print(f'First parent matrix {parent}')

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    print(f'A and B : {a} and {b}')
    parent[find(a)] = find(b)
    print(f'Iterations : {parent}')

for r in range(n):
    for c in range(m):
        if grid[r][c] != '.':
            digit[r*m + c] = int(grid[r][c])





for r in range(n):
    c = 0
    while c < m:
        if grid[r][c] == '.':
            c += 1
            continue
        start = c
        while c < m and grid[r][c] != '.':
            c += 1
        for k in range((c-start)//2):
            print(f'Val of K {k}')            
            union(r*m + start + k, r*m + c-1 - k)   #first iteration ma union(2,3)
            
print(parent)


for c in range(m):
    r = 0
    while r < n:
        if grid[r][c] == '.':
            r += 1
            continue
        start = r
        while r < n and grid[r][c] != '.':
            r += 1
        for k in range((r-start)//2):
            union((start+k)*m + c, (start + r - start - 1 - k)*m + c)

groups = {}
for i in range(n*m):
    if grid[i//m][i%m] != '.':
        root = find(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(i)

result = ['.'] * (n*m)
for cells in groups.values():
    values = [digit[i] for i in cells]
    best = min(range(10), key=lambda d: (sum(abs(v-d) for v in values), d))
    for i in cells:
        result[i] = str(best)

for r in range(n):
    print(''.join(result[r*m + c] if grid[r][c] != '.' else '.' for c in range(m)))
