import random

# Print Intro and Instructions
print("*** HANGMAN ***")
print("\nGuess letters one at a time and try to solve the phrase!")
print("Enter '1' to attempt to solve")

# Define hangman images
hangman = [
    "  _____\n   \  |\n    \ |\n     \|\n      |\n      |\n_________",
    "  _____\n O \  |\n    \ |\n     \|\n      |\n      |\n_________",
    "  _____\n O \  |\n |  \ |\n     \|\n      |\n      |\n_________",
    "  _____\n O \  |\n-|  \ |\n     \|\n      |\n      |\n_________",
    "  _____\n O \  |\n-|- \ |\n     \|\n      |\n      |\n_________",
    "  _____\n O \  |\n-|- \ |\n/    \|\n      |\n      |\n_________",
    "  _____\n O \  |\n-|- \ |\n/ \  \|\n      |\n      |\n_________",
]
turn_limit = len(hangman)-1

# Define some words and phrases
phrases = [
    "a failing grade",
    "lifetime achievement",
    "schadenfreude",
    "unsolveable problems",
    "combinatorial explosion",
    "conditional compilation",
    "polymorphism",
    "down a rabbit hole",
    "blew the stack",
    "lambda function",
    "natural selection",
    "military intelligence",
    "government ethics",
    "impeachment inquiry",
    "general relativity"
]
current_phrase = random.choice(phrases)
correct_guesses = ""
for i in range(len(current_phrase)):
    if current_phrase[i] == " ":
        correct_guesses += " "
    else:
        correct_guesses += "_"
turn_number = 1
used_letters = {}
hangman_index = 0

def test():
    print("foo")

# Display the phrase, hangman, and used letters
def display_board():
    print("================")
    print(hangman[hangman_index])
    print(f"Turn # {turn_number}")
    print(f"Guess the phrase: {correct_guesses}")
    print(f"Used letters: {' '.join(used_letters)}")

def update_string(string, index, char):
    string_list = list(string)
    string_list[index] = char
    return "".join(string_list)

# Solve method -- test guess for solution
def attempt_solve():
    solve_guess = input("Enter your guess: ")
    if solve_guess.lower() == current_phrase:
        print("YOU WIN!")
        return True
    else:
        print("YOU LOSE!")
        return False

game_over = False
# Loop until win or loss
while (game_over == False):
    display_board()
    char = input("Enter a character:")
    if char == "1":
        game_over = attempt_solve()
    if char in used_letters:
        print("* Found a used letter, pick something you haven't already tried! *")
    else:
        used_letters[char] = char
        char_found = False
        for i in range(len(current_phrase)):
            if char == current_phrase[i]:
                char_found = True
                correct_guesses = update_string(correct_guesses, i, char)
        if char_found == False:
            hangman_index += 1
    if hangman_index == turn_limit:
        display_board()
        print("YOU LOST!")
        game_over = True
    if correct_guesses == current_phrase:
        print("YOU WON!")
        game_over = True
