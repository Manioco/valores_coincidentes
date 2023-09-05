from conincidentes import match_items, read_files

GRP = "GRP.txt"
MT = "MT.txt"
RK = "RK.txt"
todos = "todos.txt"

file_combinations = [[GRP, MT], [GRP, RK], [MT, RK], [todos, GRP], [todos, MT], [todos, RK]]

for combination in file_combinations:
    bigger, smaller = read_files(combination[0], combination[1])
    match, not_match = match_items(bigger, smaller)
    file1 = combination[0].replace('.txt', '')
    file2 = combination[1].replace('.txt', '')
    with open(f'resultado/{file1}_{file2}.txt', 'w') as f:
        f.writelines(match)
    