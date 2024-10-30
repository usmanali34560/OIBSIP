import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

# Password generation logic
def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("No character types selected for password generation.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to handle password generation in GUI
def generate_and_display_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Password length must be a positive number.")
        
        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()
        
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Function to copy password to clipboard
def copy_to_clipboard():
    password = result_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

# Setting up the GUI using Tkinter
root = tk.Tk()
root.title("Advanced Password Generator")

# Create and position GUI elements
tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)

letters_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Letters", variable=letters_var).grid(row=1, column=0, padx=10, pady=5)

numbers_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=2, column=0, padx=10, pady=5)

symbols_var = tk.BooleanVar(value=True)
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).grid(row=3, column=0, padx=10, pady=5)

tk.Button(root, text="Generate Password", command=generate_and_display_password).grid(row=4, column=0, padx=10, pady=10)
result_entry = tk.Entry(root, width=50)
result_entry.grid(row=4, column=1, padx=10, pady=10)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Start the Tkinter event loop
root.mainloop()
