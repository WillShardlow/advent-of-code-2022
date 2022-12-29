def make_nice_array(input_string):
    row_array = []
    for index in range(int(len(input_string) / 4) + 1):
        if input_string[4 * index + 1] != ' ':
            row_array.append(input_string[4 * index + 1])
        else:
            row_array.append('-')
    return row_array

with open("input.txt") as f:
    input = list(map(make_nice_array, [x.strip('\n') for x in f.readlines()]))

input.reverse()

stacks = [[] for _ in range(9)]

for i in range(len(input)):
    for j in range(9):
        if input[i][j] != '-':
            stacks[j].append(input[i][j])

with open("steps.txt") as f:
    steps = [x.strip('\n') for x in f.readlines()]

steps = [step.strip('move').replace('from', '').replace('to','').replace(' ','') for step in steps]

def move_box(from_stack, to_stack):
    box = stacks[int(from_stack)].pop()
    stacks[int(to_stack)].append(box)

for step in steps:
    for repeats in range(int(step[0])):
        move_box(step[1], step[2])

if __name__ == '__main__':
    print(input[0])
    print(stacks)

