with open("input.txt") as f:
    input = f.readlines()[0]

def has_repeated_character(substring):
    for character in substring:
        if substring.count(character) > 1:
            return True
    return False

def find_first_marker(buffer):
    for index in range(3, len(buffer)):
        if not has_repeated_character(buffer[(index - 3):(index+1)]):
            return index + 1


if __name__ == '__main__':
    print(input)
    print(find_first_marker(input))
