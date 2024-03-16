{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "59477ce2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sudoku solved:\n",
      "5 3 4 6 7 8 9 1 2\n",
      "6 7 2 1 9 5 3 4 8\n",
      "1 9 8 3 4 2 5 6 7\n",
      "8 5 9 7 6 1 4 2 3\n",
      "4 2 6 8 5 3 7 9 1\n",
      "7 1 3 9 2 4 8 5 6\n",
      "9 6 1 5 3 7 2 8 4\n",
      "2 8 7 4 1 9 6 3 5\n",
      "3 4 5 2 8 6 1 7 9\n"
     ]
    }
   ],
   "source": [
    "def print_board(board):\n",
    "    for row in board:\n",
    "        print(\" \".join(str(num) for num in row))\n",
    "\n",
    "def is_valid_move(board, row, col, num):\n",
    "    # Check row\n",
    "    if num in board[row]:\n",
    "        return False\n",
    "\n",
    "    # Check column\n",
    "    if num in [board[i][col] for i in range(9)]:\n",
    "        return False\n",
    "\n",
    "    # Check 3x3 square\n",
    "    start_row, start_col = 3 * (row // 3), 3 * (col // 3)\n",
    "    for i in range(start_row, start_row + 3):\n",
    "        for j in range(start_col, start_col + 3):\n",
    "            if board[i][j] == num:\n",
    "                return False\n",
    "\n",
    "    return True\n",
    "\n",
    "def solve_sudoku(board):\n",
    "    empty_cell = find_empty_cell(board)\n",
    "    if not empty_cell:\n",
    "        return True\n",
    "\n",
    "    row, col = empty_cell\n",
    "    for num in range(1, 10):\n",
    "        if is_valid_move(board, row, col, num):\n",
    "            board[row][col] = num\n",
    "            if solve_sudoku(board):\n",
    "                return True\n",
    "            board[row][col] = 0\n",
    "\n",
    "    return False\n",
    "\n",
    "def find_empty_cell(board):\n",
    "    for i in range(9):\n",
    "        for j in range(9):\n",
    "            if board[i][j] == 0:\n",
    "                return (i, j)\n",
    "    return None\n",
    "\n",
    "# Example Sudoku board (0 represents empty cells)\n",
    "board = [\n",
    "    [5, 3, 0, 0, 7, 0, 0, 0, 0],\n",
    "    [6, 0, 0, 1, 9, 5, 0, 0, 0],\n",
    "    [0, 9, 8, 0, 0, 0, 0, 6, 0],\n",
    "    [8, 0, 0, 0, 6, 0, 0, 0, 3],\n",
    "    [4, 0, 0, 8, 0, 3, 0, 0, 1],\n",
    "    [7, 0, 0, 0, 2, 0, 0, 0, 6],\n",
    "    [0, 6, 0, 0, 0, 0, 2, 8, 0],\n",
    "    [0, 0, 0, 4, 1, 9, 0, 0, 5],\n",
    "    [0, 0, 0, 0, 8, 0, 0, 7, 9]\n",
    "]\n",
    "\n",
    "if solve_sudoku(board):\n",
    "    print(\"Sudoku solved:\")\n",
    "    print_board(board)\n",
    "else:\n",
    "    print(\"No solution exists\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1ec5c6db",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
