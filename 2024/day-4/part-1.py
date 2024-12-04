def get_columns(lines):
    columns = list(lines[0])
    for line in lines[1:]:
        columns = [col_item + line_item for col_item, line_item in zip(columns, line)]
    return columns

def get_diagonals(lines):
    diagonals = []
    def append_to_diagonals(diagonals, diagonal):
        if len(diagonal) > 3: # XMAS has 4 letters
            diagonals.append(diagonal)

    last_index = len(lines[0]) - 1
    for i in range(len(lines)):
        diagonal_row_forward = lines[i][0]
        diagonal_col_forward = lines[0][i]
        diagonal_row_backward = lines[i][last_index]
        diagonal_col_backward = lines[0][last_index - i]
        for j in range(i + 1, len(lines[0])):
            diagonal_row_forward += lines[j][j - i]
            diagonal_col_forward += lines[j - i][j]
            diagonal_row_backward += lines[j][last_index - j + i]
            diagonal_col_backward += lines[j - i][last_index - j]
        append_to_diagonals(diagonals, diagonal_row_forward)
        append_to_diagonals(diagonals, diagonal_row_backward)
        if i > 0: # prevent duplicates
            append_to_diagonals(diagonals, diagonal_col_forward)
            append_to_diagonals(diagonals, diagonal_col_backward)
    return diagonals

def count_occurences(strings_list):
    return sum(s.count('XMAS') + s.count('SAMX') for s in strings_list)


with open('input.txt') as f:
    rows = [line.strip() for line in f.readlines()]

columns = get_columns(rows)
diagonals = get_diagonals(rows)
print(count_occurences(rows + columns + diagonals))
