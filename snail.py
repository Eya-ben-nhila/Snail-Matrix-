def spiral_order(matrix):
    
    if not matrix or not matrix[0]:
        return []
    
    n = len(matrix)
    result = []
    
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    
    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    
    return result


def print_spiral_with_path(matrix):
    
    if not matrix or not matrix[0]:
        return
    
    n = len(matrix)
    order = [[0] * n for _ in range(n)]
    
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    counter = 1
    
    positions = []
    
    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            order[top][col] = counter
            positions.append((top, col))
            counter += 1
        top += 1
        
        for row in range(top, bottom + 1):
            order[row][right] = counter
            positions.append((row, right))
            counter += 1
        right -= 1
        
        if top <= bottom:
            for col in range(right, left - 1, -1):
                order[bottom][col] = counter
                positions.append((bottom, col))
                counter += 1
            bottom -= 1
        
        if left <= right:
            for row in range(bottom, top - 1, -1):
                order[row][left] = counter
                positions.append((row, left))
                counter += 1
            left += 1
    
    arrows = [['' for _ in range(n)] for _ in range(n)]
    
    for i in range(len(positions) - 1):
        curr_row, curr_col = positions[i]
        next_row, next_col = positions[i + 1]
        
        if next_col > curr_col:
            arrows[curr_row][curr_col] = '→'
        elif next_col < curr_col:
            arrows[curr_row][curr_col] = '←'
        elif next_row > curr_row:
            arrows[curr_row][curr_col] = '↓'
        elif next_row < curr_row:
            arrows[curr_row][curr_col] = '↑'
    
    last_row, last_col = positions[-1]
    arrows[last_row][last_col] = '●'
    
    print("╔" + "═" * 40 + "╗")
    print("║" + "   ORIGINAL MATRIX".center(40) + "║")
    print("╚" + "═" * 40 + "╝")
    for row in matrix:
        print("    " + " ".join(f"{val:4}" for val in row))
    
    print("\n╔" + "═" * 40 + "╗")
    print("║" + "   SNAIL PATH (with arrows)".center(40) + "║")
    print("╚" + "═" * 40 + "╝")
    for i in range(n):
        row_str = "    "
        for j in range(n):
            row_str += f"{matrix[i][j]:2}{arrows[i][j]:1} "
        print(row_str)
    
    print("\n╔" + "═" * 40 + "╗")
    print("║" + "   TRAVERSAL ORDER".center(40) + "║")
    print("╚" + "═" * 40 + "╝")
    for row in order:
        print("    " + " ".join(f"{val:4}" for val in row))
    
    result = spiral_order(matrix)
    print("\n╔" + "═" * 40 + "╗")
    print("║" + "   RESULT ARRAY".center(40) + "║")
    print("╚" + "═" * 40 + "╝")
    print("    [", end="")
    for i, val in enumerate(result):
        if i > 0:
            print(",", end="")
        print(f" {val}", end="")
    print(" ]")


def can_split_consecutive(ch):
    
    n = len(ch)
    
    for first_len in range(1, n // 2 + 1):
        first_num_str = ch[:first_len]
        
        if first_num_str[0] == '0' and len(first_num_str) > 1:
            continue
        
        first_num = int(first_num_str)
        
        result = get_sequence_if_valid(ch, first_num)
        if result:
            return True, result
    
    return False, []


def get_sequence_if_valid(ch, start_num):
    
    pos = 0
    current_num = start_num
    sequence = []
    
    while pos < len(ch):
        current_str = str(current_num)
        
        if ch[pos:pos + len(current_str)] == current_str:
            sequence.append(current_num)
            pos += len(current_str)
            current_num += 1
        else:
            return []
    
    return sequence if len(sequence) >= 2 else []


print("\n")
print("█" * 50)
print("█" + " SPIRAL MATRIX TRAVERSAL ".center(48) + "█")
print("█" * 50)
print("\n")

print("EXAMPLE 1: 3x3 Matrix")
print("-" * 50)
matrix1 = [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]
]
print_spiral_with_path(matrix1)

print("\n\n")
print("EXAMPLE 2: 4x4 Matrix")
print("-" * 50)
matrix2 = [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
]
print_spiral_with_path(matrix2)

print("\n\n")
print("EXAMPLE 3: 5x5 Matrix")
print("-" * 50)
matrix3 = [
    [1, 2, 3, 4, 5],
    [16, 17, 18, 19, 6],
    [15, 24, 25, 20, 7],
    [14, 23, 22, 21, 8],
    [13, 12, 11, 10, 9]
]
print_spiral_with_path(matrix3)

print("\n\n")
print("█" * 50)
print("█" + " CONSECUTIVE INCREASING NUMBERS ".center(48) + "█")
print("█" * 50)
print("\n")

test_cases = ['99100', '979899100101', '123', '12', '100', '010203', '1234']

for ch in test_cases:
    is_valid, sequence = can_split_consecutive(ch)
    print(f"Input:  '{ch}'")
    print(f"Valid:  {is_valid}")
    if is_valid:
        print(f"Split:  {' -> '.join(map(str, sequence))}")
    print("-" * 50)
