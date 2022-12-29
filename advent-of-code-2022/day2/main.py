import pathlib
input_string = pathlib.Path('input.txt').read_text().split('\n')

shape_scores = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}

rock_results = {
    'X': 3,
    'Y': 6,
    'Z': 0,
}

paper_results = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

scissors_results = {
    'X': 6,
    'Y': 0,
    'Z': 3,
}

results_dict = {
    'A': rock_results,
    'B': paper_results,
    'C': scissors_results,
}


def get_score(input_string):
    return results_dict[input_string[0]][input_string[2]] + shape_scores[input_string[2]]


result_scores_by_strategy = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

my_play_for_rock = {
    'X': 'C',
    'Y': 'A',
    'Z': 'B',
}

my_play_for_paper = {
    'X': 'A',
    'Y': 'B',
    'Z': 'C',
}

my_play_for_scissors = {
    'X': 'B',
    'Y': 'C',
    'Z': 'A',
}

my_play_by_their_play = {
    'A': my_play_for_rock,
    'B': my_play_for_paper,
    'C': my_play_for_scissors,
}


def get_score_2(input_string):
    return result_scores_by_strategy[input_string[2]] + shape_scores_2[my_play_by_their_play[input_string[0]][input_string[2]]]


shape_scores_2 = {
    'A': 1,
    'B': 2,
    'C': 3,
}

if __name__ == '__main__':
    print(sum(list(map(get_score, input_string[0:len(input_string) - 1]))))
    print(sum(list(map(get_score_2, input_string[0:len(input_string) - 1]))))


