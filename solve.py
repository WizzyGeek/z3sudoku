import z3

s = z3.Solver()

a = [z3.Ints([f"Box_{row}{col}" for col in range(9)]) for row in range(9)]

# print(a)
for row in a:
    for i in row:
        s.add(i > 0, i < 10)

    for idx, i in enumerate(row): # Each row has Distinct constraint
        for j in row[idx+1:]:
            s.add(i != j)

for idx, row in enumerate(a):# Each column has Distinct constraint
    for row2 in a[idx+1:]:
        for i in range(9):
            s.add(row[i] != row2[i])

for r in range(0,7,3): # Boxes in sudoku
    for c in range(0, 7, 3):
        for i in range(9):
            for k in range(i + 1, 9):
                s.add(a[(i // 3) + r][(i % 3) + c] != a[(k // 3) + r][(k % 3) + c])

with open("test_expert.txt", "r") as fd: # Sudoku file
    for ri, i in enumerate(fd.readlines()[:9]):
        for ci, j in enumerate(i):
            if j.isdigit():
                s.add(a[ri][ci] == int(j))

from time import perf_counter
now = perf_counter()
r = s.check()
print("sat result: ", r)

if r == z3.sat:
    m = s.model()
    z = ord("0")
    for i in range(9):
        t = ""
        for j in range(9):
            t += str(m.eval(a[i][j]).as_long()) # type: ignore
        print(t)
    print("time taken to solve: ", perf_counter() - now)