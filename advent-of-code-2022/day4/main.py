with open("input.txt") as f:
    input = [x.strip() for x in f.readlines()]


def get_sets(assignment):
    index_of_first_dash = assignment.find('-')
    index_of_last_dash = assignment.rfind('-')
    index_of_comma = assignment.find(',')

    return [
        set(range(int(assignment[:index_of_first_dash]), int(assignment[index_of_first_dash + 1:index_of_comma]) + 1)),
        set(range(int(assignment[index_of_comma + 1:index_of_last_dash]),
                  int(assignment[index_of_last_dash + 1:]) + 1))]


total = 0
for i in range(len(input)):
    if get_sets(input[i])[0].issubset(get_sets(input[i])[1]) or get_sets(input[i])[1].issubset(get_sets(input[i])[0]):
        total += 1

total_part_2 = 0
for i in range(len(input)):
    if len(get_sets(input[i])[0].intersection(get_sets(input[i])[1])) != 0:
        total_part_2 += 1

if __name__ == '__main__':
    print(total)
    print(total_part_2)
