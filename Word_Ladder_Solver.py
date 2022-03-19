# This program is the individual work of David Markel

import enchant
# import random

d = enchant.Dict("en_US")

pairs_list = []
line_count = 0


word = input("Enter starting word: ")
target_word = input("Enter target word: ")

# Dictionary that will store where each word came from
parent = {word: None}

alphabet = "abcdefghijklmnopqrstuvwxyz"


def combine(list1, list2):
    """Combines two lists without duplicates
    """

    new_list = list1 + [x for x in list2 if x not in list1]
    return new_list


def l2s(list):
    """Converts list to string
    """
    temp = ""
    return temp.join(list)


def one_away(str1, str2):
    """Checks if string is
    1 letter away
    """
    diff = 0
    one_away = True

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            diff += 1

    if diff > 1:
        one_away = False
    return one_away


def Generate(str, dict):
    """takes in a string, converts to list
    returns set of every possible string made by changing one letter
    """

    temp_list = []

    # Turn string into list
    str_copy = list(str)
    # Copy original str as list
    og = str_copy.copy()

    # Cycle through every digit
    for i in range(len(str_copy)):
        str_copy = og.copy()

        # Replace digit with every letter
        for x in range(len(alphabet)):
            str_copy[i] = alphabet[x]

            # Check if real word
            if ((d.check(l2s(str_copy))) and (l2s(str_copy) != str) and
                    (l2s(str_copy) not in temp_list)):

                temp_list.append(l2s(str_copy))

                # Store what word generated the word
                if l2s(str_copy) not in parent:
                    dict.update({l2s(str_copy): l2s(og)})

    return temp_list


# Main loop
run = True

# List of words that are tried
word_list = [word]

# Count generations
counter = 0

# Words that have already been checked
already_checked = []

while run:
    counter += 1
    temp_list1 = []
    temp_list2 = []

    for str in word_list:
        if str not in already_checked:

            # Check if word is one letter away from target to save time
            if one_away(str, target_word):
                parent.update({target_word: str})
                word_list.append(target_word)
                break

            temp_list1 = Generate(str, parent).copy()

            # Add newly generated words with no duplicates
            temp_list2 = combine(temp_list2, temp_list1)
            already_checked.append(str)

    # Add new batch of words
    word_list = combine(word_list, temp_list2)

    # If target is reached
    if target_word in word_list:
        run = False


# now equals how many words in between
counter -= 1

# Print solution
t_word = target_word

solution = []

while t_word != word:
    solution.append(t_word)
    t_word = parent.get(t_word)

solution.reverse()

print(word + ' -> ', end='')

for i in range(len(solution)):
    if i != len(solution) - 1:
        print(solution[i] + " -> ", end='')
    else:
        print(solution[i], end='')
