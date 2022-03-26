#
#
# stages  = ["""
#   +---+
#   |   |
#   o   |
#  /|\  |
#  / \  |
#       |
# ==========
# ""","""
#   +---+
#   |   |
#   o   |
#  /|\  |
#  /    |
#       |
# ==========
#
# ""","""
#   +---+
#   |   |
#   o   |
#  /|\  |
#       |
#       |
# ==========
# ""","""
#   +---+
#   |   |
#   o   |
#  /|   |
#       |
#       |
# ==========
# ""","""
#   +---+
#   |   |
#   o   |
#   |   |
#       |
#       |
# ==========
# ""","""
#   +---+
#   |   |
#   o   |
#       |
#       |
#       |
# ==========
# ""","""
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# ==========
# """]
#
# # step1
# import random
#
#
# end_of_game = False
# word_list = ["advark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)
#
#
# lives = 6
#
#
# print(f"Yasaladigan soz {chosen_word}")
#
# display = []
# for _ in range(word_length):
#     display += "_"
#
# while not end_of_game:
#     gues = input("Gues a letter: ").lower()
#
#     for postion in range(word_length):
#         letter = chosen_word[postion]
#         # print(f"Current postion: {postion}\n"
#         #       f"Current letter: {letter}\n"
#         #       f"Guessed letter: {gues}")
#         if letter == gues:
#             display[postion] = letter
#         # else:
#         #     print("No Match")
#
#     if gues not in chosen_word:
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("You Lose.")
#
#     print(f"{' '.join(display)}")
#
#     if "_" not in display:
#         end_of_game = True
#         print("You Win!!!")
#
#     print(stages[lives])

#
# son = input("Son kiriting: ")
#
# if son.isdigit():
#     son=int(son)
#     if son%3==0 and son%5==0:
#         print("FizzBuzz")
#     elif son % 5 == 0:
#         print("Buzz")
#     elif son % 3 == 0:
#         print("Fizz")
#     else:
#         print(son)
# else:
#     print("Siz son kiritmadingiz")
