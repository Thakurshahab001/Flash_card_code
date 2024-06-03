import random
from tkinter import *
from tkinter import PhotoImage
import pandas as pd

# Constants
BACKGROUND_COLOR = "#B1DDC6"
WORDS_TO_LEARN_FILE = "words_to_learn.csv"
FRENCH_WORDS_FILE = "french_words.csv"

# ==============================Logic========================================
# Load words
try:
    data = pd.read_csv(WORDS_TO_LEARN_FILE)
except FileNotFoundError:
    try:
        data = pd.read_csv(FRENCH_WORDS_FILE)
    except FileNotFoundError:
        print(f"Error: {FRENCH_WORDS_FILE} file not found.")
        exit()
    except pd.errors.EmptyDataError:
        print(f"Error: {FRENCH_WORDS_FILE} is empty.")
        exit()
    except Exception as e:
        print(f"Unexpected error reading {FRENCH_WORDS_FILE}: {e}")
        exit()
except pd.errors.EmptyDataError:
    print(f"Error: {WORDS_TO_LEARN_FILE} is empty.")
    exit()
except Exception as e:
    print(f"Unexpected error reading {WORDS_TO_LEARN_FILE}: {e}")
    exit()

to_learn = data.to_dict(orient="records")
current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # Cancel the previous timer
    if to_learn:
        current_card = random.choice(to_learn)
        canvas.itemconfig(card_title, text="French", fill="black")
        canvas.itemconfig(card_word, text=current_card["French"], fill="black")
        canvas.itemconfig(card_background, image=card_front_img)
        flip_timer = window.after(3000, flip_card)  # Set a new timer
    else:
        canvas.itemconfig(card_title, text="No more words!", fill="black")
        canvas.itemconfig(card_word, text="", fill="black")
        canvas.itemconfig(card_background, image=card_front_img)

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    global current_card
    try:
        to_learn.remove(current_card)
        new_data = pd.DataFrame(to_learn)
        new_data.to_csv(WORDS_TO_LEARN_FILE, index=False)
    except ValueError:
        print("Error: current_card not found in to_learn.")
    except Exception as e:
        print(f"Unexpected error updating {WORDS_TO_LEARN_FILE}: {e}")
    next_card()

# ==============================UI DESIGN=======================================================
# Window setup
window = Tk()
window.title("Flashy")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip_card)  # Initial flip timer

# Canvas setup for the flashcard front
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="card_front.png")
card_back_img = PhotoImage(file="card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Adding button for right answer
right_img = PhotoImage(file="right.png")
right_button = Button(image=right_img, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)

# Adding button for wrong answer
wrong_img = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

# Display the first card
next_card()

# Start the Tkinter event loop
window.mainloop()
