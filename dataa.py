from collections import deque

def read_input():
    N, M = map(int, input().split())
    grid = [input().strip() for _ in range(N)]
    return N, M, grid

def divide_into_sheets(grid, N, M):
    sheets = []
    for i in range(0, N, M):
        for j in range(0, N, M):
            sheet = [grid[x][j:j+M] for x in range(i, i+M)]
            sheets.append(sheet)
    return sheets

def reconstruct_map(sheets, M, N):
    num_sheets = N // M
    rearranged = [[None for _ in range(num_sheets)] for _ in range(num_sheets)]
    
    for idx, sheet in enumerate(sheets):
        flattened = ''.join(''.join(row) for row in sheet)
        if 'S' in flattened:
            rearranged[0][0] = sheet
        elif 'D' in flattened:
            rearranged[-1][-1] = sheet
        else:
            for i in range(num_sheets):
                for j in range(num_sheets):
                    if rearranged[i][j] is None:
                        rearranged[i][j] = sheet
                        break
                else:
                    continue
                break
    return rearranged

def build_full_map(rearranged, M, N):
    full_map = []
    for row in rearranged:
        for i in range(M):
            full_map.append(''.join(sheet[i] for sheet in row))
    return full_map

def find_coordinates(grid, target):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == target:
                return (i, j)
    return None

def bfs(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(start[0], start[1], 0)])  # (x, y, distance)
    visited = set()
    visited.add((start[0], start[1]))

    while queue:
        x, y, dist = queue.popleft()
        if (x, y) == end:
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] in ('T', 'D'):
                visited.add((nx, ny))
                queue.append((nx, ny, dist + 1))
    return -1  # No path found

def main():
    N, M, grid = read_input()
    sheets = divide_into_sheets(grid, N, M)
    rearranged = reconstruct_map(sheets, M, N)
    full_map = build_full_map(rearranged, M, N)
    start = find_coordinates(full_map, 'S')
    end = find_coordinates(full_map, 'D')
    shortest_distance = bfs(full_map, start, end)
    print(shortest_distance)

if __name__ == "__main__":
    main()

   