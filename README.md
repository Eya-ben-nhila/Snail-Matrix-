Problem Solving Project
This project contains solutions to two algorithmic problems implemented in Python.
1. Snail Matrix Traversal
Traverses a square n×n matrix in clockwise spiral order, starting from the top-left corner and moving inward layer by layer.
Algorithm: Uses four boundary pointers to track traversal limits. Moves right, down, left, up in sequence while shrinking boundaries after each direction.
Complexity: O(n²) time, O(1) space
Example:
Input:  [[1,2,3],
         [4,5,6],
         [7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
2. Consecutive Increasing Numbers
Determines if a string of digits can be split into at least two consecutive integers where each number is exactly 1 greater than the previous.
Algorithm: Tries all possible lengths for the first number, then attempts to build a valid sequence. Handles leading zeros validation.
Complexity: O(n²) time, O(n) space
Example:
Input:  "979899100101"
Output: True
Split:  [97, 98, 99, 100, 101]
Usage
Run the Python file to see test cases and outputs for both problems.
