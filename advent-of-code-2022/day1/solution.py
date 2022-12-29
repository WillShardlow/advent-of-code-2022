import pathlib
input_strings = pathlib.Path('input.txt').read_text().split('\n\n')

list_of_calories = [0] * len(input_strings)


def to_int(string):
    return int(string)


for index in range(len(input_strings)):
    list_of_calories[index] = map(to_int, input_strings[index].split('\n'))

list_of_total_calories = list(map(sum, list_of_calories))

print(input_strings)

sorted_list_of_total_calories = sorted(list_of_total_calories, reverse=True)
print(sorted_list_of_total_calories[0])
print(sorted_list_of_total_calories[0] +
      sorted_list_of_total_calories[1] + sorted_list_of_total_calories[2])
