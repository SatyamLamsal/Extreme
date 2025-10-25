
import sys

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        return
    parts = data[0].strip().split()
    if len(parts) < 2:
        return
    n = int(parts[0]); m = int(parts[1])
    grid = [list(line.rstrip('\n')) for line in data[1:1+n]]

    N = n*m
    parent = [-1] * N
    digit = [-1] * N

    def idx(r,c):
        return r*m + c

    for r in range(n):
        row = grid[r]
        for c in range(m):
            ch = row[c]
            i = idx(r,c)
            if ch == '.':
                parent[i] = -1
            else:
                parent[i] = i
                digit[i] = ord(ch) - ord('0')

    # union-find
    def find(x):
        # iterative with path compression
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a,b):
        if a == b:
            return
        ra = find(a); rb = find(b)
        if ra == rb:
            return
        parent[rb] = ra

    # rows: for each contiguous segment of digits, union symmetric pairs
    for r in range(n):
        c = 0
        while c < m:
            if grid[r][c] == '.':
                c += 1
                continue
            start = c
            while c < m and grid[r][c] != '.':
                c += 1
            length = c - start
            for k in range(length // 2):
                a = idx(r, start + k)
                b = idx(r, start + length - 1 - k)
                union(a,b)

    # columns
    for c in range(m):
        r = 0
        while r < n:
            if grid[r][c] == '.':
                r += 1
                continue
            start = r
            while r < n and grid[r][c] != '.':
                r += 1
            length = r - start
            for k in range(length // 2):
                a = idx(start + k, c)
                b = idx(start + length - 1 - k, c)
                union(a,b)

    # collect components
    comps = {}
    for i in range(N):
        if parent[i] == -1:
            continue
        r = find(i)
        if r not in comps:
            comps[r] = []
        comps[r].append(i)

    # compute best digit per component
    final = ['.'] * N
    for r, cells in comps.items():
        # gather original digits
        vals = [digit[i] for i in cells]
        best_cost = None
        best_d = 0
        # try digits 0..9
        for d in range(10):
            cost = 0
            for v in vals:
                cost += abs(v - d)
            if best_cost is None or cost < best_cost or (cost == best_cost and d < best_d):
                best_cost = cost
                best_d = d
        ch = chr(ord('0') + best_d)
        for i in cells:
            final[i] = ch

    # output
    out_lines = []
    for r in range(n):
        row_chars = []
        for c in range(m):
            i = idx(r,c)
            if parent[i] == -1:
                row_chars.append('.')
            else:
                row_chars.append(final[i])
        out_lines.append(''.join(row_chars))
    sys.stdout.write('\n'.join(out_lines))

main()
