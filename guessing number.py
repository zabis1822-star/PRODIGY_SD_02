import random
import tkinter as tk
from tkinter import messagebox

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        
        self.title_label = tk.Label(
            root, text="Guess the Number (1 - 100)", font=("Arial", 16, "bold")
        )
        self.title_label.pack(pady=15)

        
        self.entry = tk.Entry(root, font=("Arial", 14), justify="center")
        self.entry.pack(pady=10)

        
        self.guess_button = tk.Button(
            root, text="Submit Guess", font=("Arial", 12), command=self.check_guess
        )
        self.guess_button.pack(pady=5)

        
        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        
        self.attempt_label = tk.Label(root, text="Attempts: 0", font=("Arial", 10))
        self.attempt_label.pack()

        
        self.reset_button = tk.Button(
            root, text="Restart Game", command=self.reset_game
        )
        self.reset_button.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1
            self.attempt_label.config(text=f"Attempts: {self.attempts}")

            if guess < self.secret_number:
                self.result_label.config(text="Too Low!", fg="blue")
            elif guess > self.secret_number:
                self.result_label.config(text="Too High!", fg="red")
            else:
                messagebox.showinfo(
                    "Correct!",
                    f"You guessed it in {self.attempts} attempts!"
                )
                self.reset_game()

        except ValueError:
            self.result_label.config(text="Enter a valid number!", fg="orange")

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.attempt_label.config(text="Attempts: 0")


root = tk.Tk()
app = GuessingGame(root)
root.mainloop()
