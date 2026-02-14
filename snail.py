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
        
        if is_valid_sequence(ch, first_num):
            return True
    
    return False


def is_valid_sequence(ch, start_num):
    
    pos = 0
    current_num = start_num
    count = 0
    
    while pos < len(ch):
        current_str = str(current_num)
        
        if ch[pos:pos + len(current_str)] == current_str:
            pos += len(current_str)
            current_num += 1
            count += 1
        else:
            return False
    
    return count >= 2


print("=== Consecutive Increasing Numbers ===")
print(f"ch='99100': {can_split_consecutive('99100')}") 
print(f"ch='979899100101': {can_split_consecutive('979899100101')}")  
print(f"ch='123': {can_split_consecutive('123')}")  
print(f"ch='12': {can_split_consecutive('12')}")  
print(f"ch='100': {can_split_consecutive('100')}")  
print(f"ch='010203': {can_split_consecutive('010203')}")  

print("\n=== Spiral Matrix Traversal ===")
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Matrix:\n{matrix1}")
print(f"Spiral order: {spiral_order(matrix1)}")

matrix2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(f"\nMatrix:\n{matrix2}")
print(f"Spiral order: {spiral_order(matrix2)}")

