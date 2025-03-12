import random
import pandas as pd
from tkinter import *
import os

BACKGROUND_COLOR = "#B1DDC6"
FONT = "Ariel"
random_word = {}

#------------------------ Data Reading ------------------------#

# Function to load words from the correct file (either from 'words_to_learn.csv' or 'german_words.csv')
def load_words():
    if os.path.exists("data/words_to_learn.csv"):
        # If words_to_learn.csv exists, use it
        df = pd.read_csv("data/words_to_learn.csv", header=None)
    else:
        # Otherwise, use the original german_words.csv
        df = pd.read_csv("data/german_words.csv", header=None)

    # Filter out any rows that don't have exactly two columns
    df = df.dropna()  # Drop any rows with NaN values (if any)
    df = df[df.apply(lambda row: len(row) == 2, axis=1)]  # Ensure that each row has exactly two columns

    return df

# Load words
df = load_words()

# Convert the DataFrame to a list of tuples (German word, translation)
word_list = df.values.tolist()

#------------------------ Generating Random Word ------------------------#
def generate_word():
    global random_word
    random_word = random.choice(word_list)
    german_word = random_word[0]
    translation = random_word[1]
    return german_word, translation

#------------------------ Selecting German Word ------------------------#
def show_german_word():
    wrong_button.config(state="disabled")
    right_button.config(state="disabled")
    german_word, translation = generate_word()
    canvas.create_image(400, 263, image=card_front)
    canvas.create_text(400, 150, text="German", font=(FONT, 40, "bold"))
    canvas.create_text(400, 263, text=german_word, font=(FONT, 60, "bold"))

    # Call to show translation after 3 seconds (3000 milliseconds)
    window.after(3000, show_translation, german_word, translation)

def show_translation(german_word, translation):
    canvas.create_image(400, 263, image=card_back)
    canvas.create_text(400, 150, text="English", font=(FONT, 40, "bold"), fill="white")
    canvas.create_text(400, 263, text=translation, font=(FONT, 60, "bold"), fill="white")
    wrong_button.config(state="normal")
    right_button.config(state="normal")

#------------------------ Handling Correct Answer (✅) ------------------------#
def mark_as_known():
    global word_list, random_word

    word_list.remove(random_word)
    data = pd.DataFrame(word_list)
    data.to_csv("data/words_to_learn.csv", index=False, header=False)

    # Show the next word
    show_german_word()

#------------------------ UI Design ------------------------#
window = Tk()
window.title("Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.resizable(False, False)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

# Setting Card image
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=card_front)
canvas.create_text(400, 150, text="German", font=(FONT, 40, "bold"))
canvas.create_text(400, 263, text="Text", font=(FONT, 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Setting wrong image
wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=show_german_word)
wrong_button.grid(row=1, column=0)

# Setting right image (✅)
right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, command=mark_as_known)  # This button marks the word as known
right_button.grid(row=1, column=1)

# Start by showing a random word
show_german_word()

window.mainloop()
