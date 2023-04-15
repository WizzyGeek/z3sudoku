# Z3 Sudoku Solving

This reposistory solves the sudoku puzzle by simply supplying 162 domain restriction contraints `0 < x, x < 10`
and 972 Distinct constraints.

The code is fairly basic and (I believe) can be read by anyone familiar with logic and code.

The method seems to be quite fast and can be extended easily to find all solutions to a sudoku puzzle

### The logic

1. Make 81 variables
2. Place Uniqueness constraints for row, column and 3x3 box the variable belongs to
3. Read a sudoku, and set a equality constraints for all hints in the sudoku
4. Check satisfiability with z3
5. Get one of the solutions to the puzzle if one exists.

<hr/>
<div align="center"><i>There is nothing to copyright but,<br/>
Copyright 2023, WizzyGeek</i></div>