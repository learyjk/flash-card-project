from tkinter import *
from PIL import ImageTk, Image
import json

BACKGROUND_COLOR = "#B1DDC6"


window = Tk()
window.title("Flash Cards")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = ImageTk.PhotoImage(Image.open("images/card_front.gif"))
canvas.create_image(400, 263, image=card_front_img)
canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas.create_text(400, 300, text="trouve", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_img = ImageTk.PhotoImage(Image.open("images/wrong.gif"))
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(column=0, row=1)

correct_img = ImageTk.PhotoImage(Image.open("images/right.gif"))
correct_button = Button(image=correct_img, highlightthickness=0)
correct_button.grid(column=1, row=1)

window.mainloop()
