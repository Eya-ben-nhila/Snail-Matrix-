import pygame
import sys

def spiral_order_with_positions(matrix):
    
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
    
    return positions


def animate_spiral_matrix(matrix):
    
    pygame.init()
    
    n = len(matrix)
    cell_size = 150
    margin = 80
    width = n * cell_size + 2 * margin
    height = n * cell_size + 2 * margin + 150
    
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Snail Matrix Traversal Animation")
    
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (200, 200, 200)
    BLUE = (100, 150, 255)
    GREEN = (100, 255, 150)
    RED = (255, 100, 100)
    
    font_large = pygame.font.Font(None, 64)
    font_small = pygame.font.Font(None, 36)
    
    positions = spiral_order_with_positions(matrix)
    visited = set()
    current_index = 0
    
    clock = pygame.time.Clock()
    running = True
    paused = False
    speed = 1
    auto_play = True
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
                elif event.key == pygame.K_r:
                    current_index = 0
                    visited = set()
                elif event.key == pygame.K_UP:
                    speed = min(speed + 1, 10)
                elif event.key == pygame.K_DOWN:
                    speed = max(speed - 1, 1)
        
        screen.fill(WHITE)
        
        for i in range(n):
            for j in range(n):
                x = margin + j * cell_size
                y = margin + i * cell_size
                
                if (i, j) in visited:
                    color = GREEN
                elif current_index < len(positions) and positions[current_index] == (i, j):
                    color = RED
                else:
                    color = GRAY
                
                pygame.draw.rect(screen, color, (x, y, cell_size, cell_size))
                pygame.draw.rect(screen, BLACK, (x, y, cell_size, cell_size), 4)
                
                text = font_large.render(str(matrix[i][j]), True, BLACK)
                text_rect = text.get_rect(center=(x + cell_size // 2, y + cell_size // 2))
                screen.blit(text, text_rect)
        
        if current_index > 0:
            for idx in range(current_index):
                if idx < len(positions) - 1:
                    row1, col1 = positions[idx]
                    row2, col2 = positions[idx + 1]
                    
                    x1 = margin + col1 * cell_size + cell_size // 2
                    y1 = margin + row1 * cell_size + cell_size // 2
                    x2 = margin + col2 * cell_size + cell_size // 2
                    y2 = margin + row2 * cell_size + cell_size // 2
                    
                    pygame.draw.line(screen, BLUE, (x1, y1), (x2, y2), 6)
        
        result_text = "Result: ["
        for idx in range(current_index):
            if idx < len(positions):
                row, col = positions[idx]
                result_text += str(matrix[row][col])
                if idx < current_index - 1:
                    result_text += ", "
        result_text += "]"
        
        result_surface = font_small.render(result_text, True, BLACK)
        screen.blit(result_surface, (margin, height - 120))
        
        controls = f"SPACE: Pause/Play | R: Restart | UP/DOWN: Speed ({speed})"
        controls_surface = font_small.render(controls, True, BLACK)
        screen.blit(controls_surface, (margin, height - 80))
        
        progress = f"Progress: {current_index}/{len(positions)}"
        progress_surface = font_small.render(progress, True, BLACK)
        screen.blit(progress_surface, (margin, height - 40))
        
        if paused:
            pause_text = font_large.render("PAUSED", True, RED)
            screen.blit(pause_text, (width // 2 - 100, 10))
        
        pygame.display.flip()
        
        if not paused and current_index < len(positions):
            visited.add(positions[current_index])
            current_index += 1
            clock.tick(speed)
        elif current_index >= len(positions):
            clock.tick(30)
        else:
            clock.tick(30)
    
    pygame.quit()


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
    print("\n" + "=" * 60)
    print("PROBLEM 1: SNAIL MATRIX TRAVERSAL")
    print("=" * 60)
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
    elif choice == "2":
        matrix = [
            [1, 2, 3, 4],
            [12, 13, 14, 5],
            [11, 16, 15, 6],
            [10, 9, 8, 7]
        ]
    elif choice == "3":
        matrix = [
            [1, 2, 3, 4, 5],
            [16, 17, 18, 19, 6],
            [15, 24, 25, 20, 7],
            [14, 23, 22, 21, 8],
            [13, 12, 11, 10, 9]
        ]
    else:
        print("Invalid choice. Using 3x3 matrix.")
        matrix = [
            [1, 2, 3],
            [8, 9, 4],
            [7, 6, 5]
        ]
    
    print("\nThe animation will start...")
    print("Controls:")
    print("  SPACE - Pause/Resume")
    print("  R - Restart")
    print("  UP/DOWN - Adjust speed")
    print("\nClose the window when done to continue to Problem 2")
    
    animate_spiral_matrix(matrix)
    
    print("\n" + "=" * 60)
    print("PROBLEM 2: CONSECUTIVE INCREASING NUMBERS")
    print("=" * 60)
    
    test_cases = ['99100', '979899100101', '123', '12', '100', '010203', '1234', '91011']
    
    for ch in test_cases:
        is_valid, sequence = can_split_consecutive(ch)
        print(f"\nInput:  '{ch}'")
        print(f"Valid:  {is_valid}")
        if is_valid:
            print(f"Split:  {' -> '.join(map(str, sequence))}")
        print("-" * 60)
    
    print("\nProgram completed!")
