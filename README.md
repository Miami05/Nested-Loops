
# Multiplication Table & Triangle Pattern Generator

A simple Python CLI application that generates formatted multiplication tables and number triangle patterns based on user input.

## Features

- **Multiplication Table Generator**: Creates a formatted n×n multiplication table
- **Triangle Pattern Generator**: Prints ascending and descending number triangles
- **Interactive CLI**: Continuous loop for multiple operations until exit

## Functions

### `print_multiplication_table(n)`
Generates and displays an n×n multiplication table with aligned columns.

**Parameters:**
- `n` (int): Size of the multiplication table

**Example Output** (n=5):
  1   2   3   4   5 
1 1 2 3 4 5  
2 2 4 6 8 10  
3 3 6 9 12 15  
4 4 8 12 16 20  
5 5 10 15 20 25

### `print_triangle(n)`
Creates a diamond-shaped number pattern that ascends to n, then descends.

**Parameters:**
- `n` (int): Maximum height of the triangle

**Example Output** (n=4):
1  
1 2  
1 2 3  
1 2 3 4  
1 2 3  
1 2  
1

## Usage

### Running the Program


### Interactive Commands

1. **Enter a number**: Input any positive integer for the pattern size
2. **Choose a command**:
   - `triangle`: Generate triangle pattern
   - `mp`: Generate multiplication table
3. **Exit**: Enter `-1` when prompted for a number

### Example Session

Please enter a number: 3  
Please enter a command (triangle/mp): triangle  
1  
1 2  
1 2 3  
1 2  
1

Please enter a number: 3  
Please enter a command (triangle/mp): mp  
1 2 3  
1 1 2 3  
2 2 4 6  
3 3 6 9

Please enter a number: -1  
Bye!

## Requirements

- Python 3.6 or higher

## Code Structure

- **Input validation**: Currently accepts any integer input
- **Formatted output**: Uses f-strings with width specifiers for alignment
- **Loop control**: Continues until user enters `-1`

## Potential Improvements

- Add input validation for non-integer values
- Handle negative numbers gracefully
- Add more pattern options (right triangles, inverted patterns)
- Implement error handling for invalid commands
- Add option to save output to file

## License

This project is licensed under the MIT License.

