contents = open("day04.txt").read()

def get_main_diagonals(rows):
    diagonals = []
    num_rows = len(rows)
    num_cols = len(rows[0])

    # Main diagonals starting from first row
    for col_start in range(num_cols):
        diagonal = "".join(rows[row][col_start + row] for row in range(min(num_rows, num_cols - col_start)))
        diagonals.append(diagonal)

    # Main diagonals starting from first column (excluding the top-left corner to avoid duplicates)
    for row_start in range(1, num_rows):
        diagonal = "".join(rows[row_start + row][row] for row in range(min(num_rows - row_start, num_cols)))
        diagonals.append(diagonal)

    return diagonals


def get_anti_diagonals(inp_rows):
    out_diagonals = []
    num_rows = len(inp_rows)
    num_cols = len(inp_rows[0])

    # Anti-diagonals starting from the first row
    for col_start in range(num_cols):
        current_diagonal = "".join(inp_rows[row][col_start - row] for row in range(min(num_rows, col_start + 1)))
        out_diagonals.append(current_diagonal)

    # Anti-diagonals starting from the last column (excluding the top-right corner to avoid duplicates)
    for row_start in range(1, num_rows):
        current_diagonal = "".join(inp_rows[row_start + row][num_cols - 1 - row] for row in range(min(num_rows - row_start, num_cols)))
        out_diagonals.append(current_diagonal)

    return out_diagonals


# Part 1

rows = contents.split("\n")
columns = ["".join([row[i] for row in rows]) for i in range(len(rows))]

diagonals = get_main_diagonals(rows) + get_anti_diagonals(rows)

result1 = 0

for line in rows:
    result1 += line.count("XMAS")
    result1 += line[::-1].count("XMAS")

for column in columns:
    result1 += column.count("XMAS")
    result1 += column[::-1].count("XMAS")

for diagonal in diagonals:
    result1 += diagonal.count("XMAS")
    result1 += diagonal[::-1].count("XMAS")

print(result1)

# Part 2
xmas_count = 0

for i in range(len(rows)):
    for j in range(len(rows)):
        try:
            if rows[i+1][j+1] != 'A':
                continue
            if rows[i][j] == 'M' and rows[i + 2][j + 2] == 'S':
                print(f"row {i} index {j}")
                print(rows[i][j], rows[i + 1][j + 1], rows[i + 2][j + 2])
                if rows[i + 2][j] == 'M' and rows[i][j + 2] == 'S':
                    xmas_count += 1
                elif rows[i + 2][j] == 'S' and rows[i][j + 2] == 'M':
                    xmas_count += 1
            if rows[i][j] == 'S' and rows[i + 2][j + 2] == 'M':
                if rows[i + 2][j] == 'M' and rows[i][j + 2] == 'S':
                    xmas_count += 1
                elif rows[i + 2][j] == 'S' and rows[i][j + 2] == 'M':
                    xmas_count += 1
                continue
        except IndexError:
            continue

print(xmas_count)
