import random
import tkinter as tk
from tkinter import simpledialog, messagebox

def number_guessing_game():
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    number_to_guess = random.randint(1, 100)
    attempts = 0

    messagebox.showinfo("Number Guessing Game", "I'm thinking of a number between 1 and 100.")

    while True:
        guess_str = simpledialog.askstring("Your Guess", "Enter your guess (1-100):")
        if guess_str is None:
            messagebox.showinfo("Game Over", "You cancelled the game.")
            break
        try:
            guess = int(guess_str)
            attempts += 1

            if guess < 1 or guess > 100:
                messagebox.showwarning("Invalid", "Please guess a number between 1 and 100.")
            elif guess < number_to_guess:
                messagebox.showinfo("Result", "Too low. Try again.")
            elif guess > number_to_guess:
                messagebox.showinfo("Result", "Too high. Try again.")
            else:
                messagebox.showinfo("Congratulations!", f"You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a valid integer.")

    root.destroy()

if __name__ == "__main__":
    number_guessing_game()