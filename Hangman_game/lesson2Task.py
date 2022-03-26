# # Hangman
#
# # step1
#
# word_list = ["advark", "baboon", "camel"]
#
# import random
#
# chosen_word = random.choice(word_list)
#
# display = []
# for _ in range(len(chosen_word)):
#     display+="_"
# print(display)
#
#
# gues = input("Gues a letter: ").lower()
#
# for letter in chosen_word:
#     if letter == gues:
#         print("To'g'ri!")
#     else:
#         print("Xato")


# # Hangman
#
# # step2
# import random
#
# word_list = ["advark", "baboon", "camel"]
#
# chosen_word = random.choice(word_list)
# print(f"{chosen_word}")
#
# display = []
# word_length = len(chosen_word)
#
# for _ in range(word_length):
#     display += "_"
# print(display)
# end_of_game = False
#
# while not end_of_game:
#     gues = input("Gues a letter: ").lower()
#
#     for postion in range(len(chosen_word)):
#         letter = chosen_word[postion]
#         if letter == gues:
#             display[postion] = letter
#
#
#     print(display)
#     if "_" not in display:
#         end_of_game = True
#         print("You Win!!!")


# # Hangman
#
# # step1
#
# word_list = ["advark", "baboon", "camel"]
#
# import random
#
# chosen_word = random.choice(word_list)
#
# display = []
# for _ in range(len(chosen_word)):
#     display+="_"
# print(display)
#
#
# gues = input("Gues a letter: ").lower()
#
# for letter in chosen_word:
#     if letter == gues:
#         print("To'g'ri!")
#     else:
#         print("Xato")


# Hangman

# step1
import random

word_list = ["advark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(f"{chosen_word}")

display = []
word_length = len(chosen_word)

for _ in range(word_length):
    display += "_"
print(display)
end_of_game = False

while not end_of_game:
    gues = input("Gues a letter: ").lower()

    for postion in range(len(chosen_word)):
        letter = chosen_word[postion]
        if letter == gues:
            display[postion] = letter

    print(display)
    if "_" not in display:
        end_of_game = True
        print("You Win!!!")
