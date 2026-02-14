import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


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


def print_matrix_animated(matrix, positions, current_index):
    
    clear_screen()
    n = len(matrix)
    
    # Build arrow matrix
    arrows = [[' ' for _ in range(n)] for _ in range(n)]
    for i in range(min(current_index, len(positions) - 1)):
        if i < len(positions) - 1:
            arrows[positions[i][0]][positions[i][1]] = get_arrow(positions[i], positions[i + 1])
    
    if current_index > 0 and current_index <= len(positions):
        last_idx = current_index - 1
        arrows[positions[last_idx][0]][positions[last_idx][1]] = '●'
    
    print("\n" + "╔" + "═" * 58 + "╗")
    print("║" + "SNAIL MATRIX TRAVERSAL".center(58) + "║")
    print("╚" + "═" * 58 + "╝\n")
    
    # Print matrix with arrows directly on it
    print("  ┌" + "─────┬" * (n - 1) + "─────┐")
    for i in range(n):
        row_str = "  │"
        for j in range(n):
            row_str += f" {matrix[i][j]:2}{arrows[i][j]} │"
        print(row_str)
        if i < n - 1:
            print("  ├" + "─────┼" * (n - 1) + "─────┤")
        else:
            print("  └" + "─────┴" * (n - 1) + "─────┘")
    
    # Build result
    result = []
    for idx in range(current_index):
        if idx < len(positions):
            row, col = positions[idx]
            result.append(matrix[row][col])
    
    print()
    print(f"  Result: {result}")
    print(f"  Progress: {current_index}/{len(positions)}")
    print()
    print("  Legend: → ↓ ← ↑ = Direction  |  ● = Current position")


def spiral_order_animated(matrix, delay=0.5):
    
    if not matrix or not matrix[0]:
        return []
    
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
    
    result = []
    
    for idx in range(len(positions) + 1):
        print_matrix_animated(matrix, positions, idx)
        time.sleep(delay)
    
    print("\n  ✓ TRAVERSAL COMPLETE!\n")
    
    for pos in positions:
        result.append(matrix[pos[0]][pos[1]])
    
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
    clear_screen()
    print("\n" + "═" * 60)
    print("PROBLEM 1: SNAIL MATRIX TRAVERSAL")
    print("═" * 60)
    print("\nChoose a matrix to visualize:")
    print("1. 3x3 Matrix")
    print("2. 4x4 Matrix")
    print("3. 5x5 Matrix")
    
    choice = input("\nEnter choice (1-3): ")
    
    if choice == "1":
        matrix = [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5]
        ]
        delay = 0.5
    elif choice == "2":
        matrix = [
            [1, 2, 3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10, 9, 8, 7]
        ]
        delay = 0.4
    elif choice == "3":
        matrix = [
            [1, 2, 3, 4, 5],
            [16, 17, 18, 19, 6],
            [15, 24, 25, 20, 7],
            [14, 23, 22, 21, 8],
            [13, 12, 11, 10, 9]
        ]
        delay = 0.3
    else:
        print("Invalid choice. Using 3x3 matrix.")
        matrix = [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5]
        ]
        delay = 0.5
    
    print("\nStarting animation in 3 seconds...")
    time.sleep(1)
    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)
    
    result = spiral_order_animated(matrix, delay)
    
    input("\nPress Enter to continue to Problem 2...")
    
    clear_screen()
    print("\n" + "═" * 60)
    print("PROBLEM 2: CONSECUTIVE INCREASING NUMBERS")
    print("═" * 60)
    
    test_cases = ['99100', '979899100101', '123', '12', '100', '010203', '1234', '91011']
    
    for ch in test_cases:
        is_valid, sequence = can_split_consecutive(ch)
        print(f"\nInput:  '{ch}'")
        print(f"Valid:  {is_valid}")
        if is_valid:
            print(f"Split:  {' -> '.join(map(str, sequence))}")
        print("-" * 60)
    
    print("\nProgram completed!")
    input("\nPress Enter to exit...")
