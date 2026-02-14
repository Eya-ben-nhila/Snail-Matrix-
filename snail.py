def spiral_order(matrix):
    """
    Return all elements of a square matrix in clockwise spiral order.
    
    Args:
        matrix: n x n list of lists containing integers
    
    Returns:
        List of integers in spiral order
    """
    if not matrix or not matrix[0]:
        return []
    
    n = len(matrix)
    result = []
    
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    
    while top <= bottom and left <= right:
        # Move right across the top row
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1
        
        # Move down the right column
        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1
        
        # Move left across the bottom row (if there's a row left)
        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1
        
        # Move up the left column (if there's a column left)
        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    
    return result

def can_split_consecutive(ch):
    """
    Check if string of digits can be split into consecutive increasing numbers.
    
    Args:
        ch: String containing only digits
    
    Returns:
        True if valid split exists, False otherwise
    """
    n = len(ch)
    
    # Try different lengths for the first number (from 1 to n//2)
    for first_len in range(1, n // 2 + 1):
        # Extract the first number
        first_num_str = ch[:first_len]
        
        # Skip if it has leading zeros (except for "0" itself, but that won't work for increasing)
        if first_num_str[0] == '0' and len(first_num_str) > 1:
            continue
        
        first_num = int(first_num_str)
        
        # Try to build the sequence
        if is_valid_sequence(ch, first_num):
            return True
    
    return False


def is_valid_sequence(ch, start_num):
    """
    Helper function to check if ch can be formed by consecutive numbers starting from start_num.
    """
    pos = 0
    current_num = start_num
    count = 0
    
    while pos < len(ch):
        current_str = str(current_num)
        
        # Check if the string at current position matches current_num
        if ch[pos:pos + len(current_str)] == current_str:
            pos += len(current_str)
            current_num += 1
            count += 1
        else:
            return False
    
    # Need at least 2 numbers for a valid sequence
    return count >= 2


# Test cases
print("=== Consecutive Increasing Numbers ===")
print(f"ch='99100': {can_split_consecutive('99100')}")  # True (99, 100)
print(f"ch='979899100101': {can_split_consecutive('979899100101')}")  # True (97, 98, 99, 100, 101)
print(f"ch='123': {can_split_consecutive('123')}")  # True (1, 2, 3)
print(f"ch='12': {can_split_consecutive('12')}")  # True (1, 2)
print(f"ch='100': {can_split_consecutive('100')}")  # False
print(f"ch='010203': {can_split_consecutive('010203')}")  # False (leading zeros)

# Test Spiral Matrix
print("\n=== Spiral Matrix Traversal ===")
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Matrix:\n{matrix1}")
print(f"Spiral order: {spiral_order(matrix1)}")
# Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]

matrix2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(f"\nMatrix:\n{matrix2}")
print(f"Spiral order: {spiral_order(matrix2)}")
# Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]