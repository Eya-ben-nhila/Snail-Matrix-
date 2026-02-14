def get_arrow(curr_pos, next_pos):
    curr_row, curr_col = curr_pos
    next_row, next_col = next_pos
    
    if next_col > curr_col:
        return '→'
    elif next_col < curr_col:
        return '←'
    elif next_row > curr_row:
        return '↓'
    elif next_row < curr_row:
        return '↑'
    return ' '


def print_matrix_with_arrows(matrix):
   
    n = len(matrix)
    positions = []
    
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    
    while top <= bottom and left <= right:
        for col in range(left, right + 1):
            positions.append((top, col))
        top += 1
        
        for row in range(top, bottom + 1):
            positions.append((row, right))
        right -= 1
        
        if top <= bottom:
            for col in range(right, left - 1, -1):
                positions.append((bottom, col))
            bottom -= 1
        
        if left <= right:
            for row in range(bottom, top - 1, -1):
                positions.append((row, left))
            left += 1
    
    arrows = [[' ' for _ in range(n)] for _ in range(n)]
    for i in range(len(positions) - 1):
        row, col = positions[i]
        arrows[row][col] = get_arrow(positions[i], positions[i + 1])
    
    print("┏" + "━━━━━┳" * (n - 1) + "━━━━━┓")
    
    for i in range(n):
        row_str = "┃"
        for j in range(n):
            if arrows[i][j]:
                row_str += f" {matrix[i][j]:2}{arrows[i][j]} ┃"
            else:
                row_str += f" {matrix[i][j]:2}  ┃"
        print(row_str)
        
        if i < n - 1:
            print("┣" + "━━━━━╋" * (n - 1) + "━━━━━┫")
        else:
            print("┗" + "━━━━━┻" * (n - 1) + "━━━━━┛")


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


if __name__ == "__main__":
    print("\nPROBLEM 1: SNAIL MATRIX TRAVERSAL")
    print("=" * 60)
    
    # Matrix from the uploaded image
    matrix = [
        [1, 2, 3, 4, 5],
        [16, 17, 18, 19, 6],
        [15, 24, 25, 20, 7],
        [14, 23, 22, 21, 8],
        [13, 12, 11, 10, 9]
    ]
    
    print("\nMatrix with Spiral Path:")
    print_matrix_with_arrows(matrix)
    
    result = spiral_order(matrix)
    print(f"\nSpiral Order: {result}")
    
    print("\n" + "=" * 60)
    print("\nPROBLEM 2: CONSECUTIVE INCREASING NUMBERS")
    print("=" * 60)
    
    test_cases = ['99100', '979899100101', '123', '12', '100', '010203', '1234', '91011']
    
    for ch in test_cases:
        is_valid, sequence = can_split_consecutive(ch)
        print(f"\nInput:  '{ch}'")
        print(f"Valid:  {is_valid}")
        if is_valid:
            print(f"Split:  {' -> '.join(map(str, sequence))}")
        print("-" * 60)
