from tkinter import *
from tkinter import PhotoImage

# Constants
BACKGROUND_COLOR = "#B1DDC6"

# Window setup
window = Tk()
window.title("Flashy")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOR)

# Canvas setup for the flashcard front
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="card_front.png")
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400,150,text="Title",font=("Arial" ,40 ,"italic"))
canvas.create_text(400,263,text="Word",font=("Arial" ,60 ,"bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Adding button for right answer
right_img = PhotoImage(file="right.png")
right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(column=1, row=1)

# Adding button for wrong answer
wrong_img = PhotoImage(file="wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(column=0, row=1)

window.mainloop()
