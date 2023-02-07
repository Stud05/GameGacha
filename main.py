import random
import json
import tkinter as tk

# Load the character data from the JSON file
with open("characters.json") as file:
    characters = json.load(file)

# Function to simulate pulling a character from the gacha
def pull_gacha():
    return random.choice(characters)

# Create the main window
root = tk.Tk()
root.title("Gacha Game")
root.geometry("500x100")
root.resizable(True, True)

# Create the "Pull" button
def pull_button_clicked():
    character = pull_gacha()
    result_label.config(text=f"You got: {character['name']} ({character['attribute']})")
    description_label.config(text=f"Description: {character['description']}")

pull_button = tk.Button(root, text="Pull", command=pull_button_clicked)
pull_button.pack()

# Create the result label
result_label = tk.Label(root, text="")
result_label.pack()

# Create the description label
description_label = tk.Label(root, text="")
description_label.pack()

# Start the GUI event loop
root.mainloop()
