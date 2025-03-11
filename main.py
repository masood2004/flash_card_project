import csv
import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Times New Roman"

#------------------------ Data Reading ------------------------#
with open("data/german_words.csv", 'r') as data_file:
    reader = csv.reader(data_file)
    word_list = []
    for row in reader:
        if len(row) == 2:
            word_list.append(row)
        else:
            print(f"Skipping malformed row: {row}")

#------------------------ Generating Random Word ------------------------#

def generate_word():
    random_word = random.choice(word_list)
    german_word = random_word[0]
    translation = random_word[1]
    return german_word, translation

#------------------------ Selecting German Word ------------------------#

def select_word():
    german_word, translation = generate_word()
    canvas.create_image(400, 263, image=card_front)
    canvas.create_text(400, 150, text="German", font=(FONT, 40, "bold"))
    canvas.create_text(400, 263, text=german_word, font=(FONT, 60, "bold"))

#------------------------ Selecting Translation ------------------------#


#------------------------ UI Design ------------------------#

window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.resizable(False, False)

# Setting Card image
card_front = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front)
canvas.create_text(400, 150, text="German", font=(FONT, 40, "bold"))
canvas.create_text(400, 263, text="Text", font=(FONT, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Setting wrong image
wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=select_word)
wrong_button.grid(row=1, column=0)

# Setting wrong image
right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, command=select_word)
right_button.grid(row=1, column=1)

window.mainloop()
