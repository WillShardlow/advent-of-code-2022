with open("input.txt") as f:
    input_string = [x.strip() for x in f.readlines()]


def get_repeated_item(rucksack):
    halfway_index = int(len(rucksack) / 2)
    first_half = rucksack[:halfway_index]
    second_half = rucksack[halfway_index:]
    return list(set(first_half).intersection(second_half))[0]


def get_badge(rucksacks):
    return list(set(rucksacks[0]).intersection((rucksacks[1])).intersection(rucksacks[2]))[0]


priorities_by_item = {}

for i in range(97, 97 + 26):
    priorities_by_item[chr(i)] = i - 96
for i in range(65, 65 + 26):
    priorities_by_item[chr(i)] = i - 64 + 26

priorities = [priorities_by_item[get_repeated_item(rucksack)] for rucksack in input_string]

list_of_groups_rucksacks = [[input_string[3 * i], input_string[3 * i + 1], input_string[3 * i + 2]] for i in range(int(len(input_string) / 3))]

priorities_part_2 = [priorities_by_item[get_badge(rucksacks)] for rucksacks in list_of_groups_rucksacks]

if __name__ == '__main__':
    print(sum(priorities))
    print(sum(priorities_part_2))
