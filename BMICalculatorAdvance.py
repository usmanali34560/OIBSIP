import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Database setup for storing user BMI data
def setup_db():
    conn = sqlite3.connect('bmi_data.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bmi_data
                 (id INTEGER PRIMARY KEY, name TEXT, weight REAL, height REAL, bmi REAL)''')
    conn.commit()
    conn.close()

# Function to calculate BMI
def calculate_bmi(weight, height):
    return weight / (height ** 2)

# Function to save BMI data to database
def save_bmi_data(name, weight, height, bmi):
    conn = sqlite3.connect('bmi_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO bmi_data (name, weight, height, bmi) VALUES (?, ?, ?, ?)",
              (name, weight, height, bmi))
    conn.commit()
    conn.close()

# Function to display historical BMI data and trends
def view_bmi_trends():
    conn = sqlite3.connect('bmi_data.db')
    c = conn.cursor()
    c.execute("SELECT name, bmi FROM bmi_data")
    data = c.fetchall()
    conn.close()

    if not data:
        messagebox.showinfo("Info", "No data available to display.")
        return

    names = [row[0] for row in data]
    bmi_values = [row[1] for row in data]

    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(names, bmi_values, marker='o', linestyle='-', color='b')
    ax.set_title("BMI Trends")
    ax.set_xlabel("User")
    ax.set_ylabel("BMI")

    # Create a new window to display the graph
    trend_window = tk.Toplevel()
    trend_window.title("BMI Trends")
    
    canvas = FigureCanvasTkAgg(fig, master=trend_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Main application class
class BMICalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator")

        # Labels and input fields
        self.label_name = tk.Label(root, text="Name:")
        self.label_name.grid(row=0, column=0, padx=10, pady=10)
        self.entry_name = tk.Entry(root)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        self.label_weight = tk.Label(root, text="Weight (kg):")
        self.label_weight.grid(row=1, column=0, padx=10, pady=10)
        self.entry_weight = tk.Entry(root)
        self.entry_weight.grid(row=1, column=1, padx=10, pady=10)

        self.label_height = tk.Label(root, text="Height (m):")
        self.label_height.grid(row=2, column=0, padx=10, pady=10)
        self.entry_height = tk.Entry(root)
        self.entry_height.grid(row=2, column=1, padx=10, pady=10)

        # Calculate BMI Button
        self.calc_button = tk.Button(root, text="Calculate BMI", command=self.calculate_bmi)
        self.calc_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # View BMI Trends Button
        self.trends_button = tk.Button(root, text="View BMI Trends", command=view_bmi_trends)
        self.trends_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    # BMI Calculation and categorization
    def calculate_bmi(self):
        try:
            name = self.entry_name.get()
            weight = float(self.entry_weight.get())
            height = float(self.entry_height.get())
            
            if not name:
                raise ValueError("Name cannot be empty.")
            if weight <= 0 or height <= 0:
                raise ValueError("Height and weight must be positive values.")
            
            bmi = calculate_bmi(weight, height)
            category = self.bmi_category(bmi)
            save_bmi_data(name, weight, height, bmi)

            # Display result
            messagebox.showinfo("BMI Result", f"Name: {name}\nBMI: {bmi:.2f}\nCategory: {category}")
        
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    # Categorize BMI
    def bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 24.9:
            return "Normal weight"
        elif 25 <= bmi < 29.9:
            return "Overweight"
        else:
            return "Obesity"

# Running the GUI application
if __name__ == "__main__":
    setup_db()
    root = tk.Tk()
    app = BMICalculatorApp(root)
    root.mainloop()
