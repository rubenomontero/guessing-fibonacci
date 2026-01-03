import tkinter as tk
from tkinter import messagebox

def generate_fibonacci_up_to(limit):
    """Generate Fibonacci numbers up to a given limit."""
    fib_sequence = [0, 1]
    while fib_sequence[-1] < limit:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def find_closest_fibonacci(number):
    """Find the closest Fibonacci number to the given number."""
    fib_sequence = generate_fibonacci_up_to(abs(number) * 2 + 100)
    closest = fib_sequence[0]
    closest_index = 0
    
    for i, fib in enumerate(fib_sequence):
        if abs(fib - abs(number)) < abs(closest - abs(number)):
            closest = fib
            closest_index = i
    
    # Get the two numbers that form this Fibonacci number
    if closest_index >= 2:
        prev1 = fib_sequence[closest_index - 1]
        prev2 = fib_sequence[closest_index - 2]
    elif closest_index == 1:
        prev1 = fib_sequence[0]
        prev2 = 0
    else:
        prev1 = 0
        prev2 = 0
    
    return closest, prev2, prev1

class FibonacciGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Fibonacci Closest Number Finder")
        self.root.geometry("600x500")
        self.root.resizable(True, True)
        
        # Title Frame
        title_frame = tk.Frame(root, bg="#8e44ad", pady=15)
        title_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            title_frame, 
            text="FIBONACCI CLOSEST NUMBER FINDER", 
            font=("Arial", 16, "bold"),
            bg="#8e44ad",
            fg="white"
        )
        title_label.pack()
        
        # Info Frame
        info_frame = tk.Frame(root, bg="#ecf0f1", pady=10)
        info_frame.pack(fill=tk.X, padx=10, pady=10)
        
        info_text = "Enter any integer and find the closest Fibonacci number to it!"
        
        info_label = tk.Label(
            info_frame,
            text=info_text,
            font=("Arial", 11),
            bg="#ecf0f1",
            justify=tk.CENTER
        )
        info_label.pack(padx=10)
        
        # Input Frame
        input_frame = tk.Frame(root, pady=20)
        input_frame.pack(fill=tk.X, padx=10)
        
        input_label = tk.Label(
            input_frame,
            text="Enter an integer:",
            font=("Arial", 12, "bold")
        )
        input_label.pack(pady=5)
        
        self.input_entry = tk.Entry(
            input_frame,
            font=("Arial", 14),
            width=25,
            justify=tk.CENTER
        )
        self.input_entry.pack(pady=5)
        self.input_entry.bind('<Return>', lambda e: self.calculate())
        
        button_frame = tk.Frame(input_frame)
        button_frame.pack(pady=10)
        
        calc_button = tk.Button(
            button_frame,
            text="Find Closest",
            font=("Arial", 12, "bold"),
            bg="#9b59b6",
            fg="white",
            command=self.calculate,
            padx=20,
            pady=5
        )
        calc_button.pack(side=tk.LEFT, padx=5)
        
        clear_button = tk.Button(
            button_frame,
            text="Clear",
            font=("Arial", 12),
            bg="#95a5a6",
            fg="white",
            command=self.clear_all,
            padx=20,
            pady=5
        )
        clear_button.pack(side=tk.LEFT, padx=5)
        
        # Result Frame
        result_frame = tk.Frame(root, bg="#f8f9fa", pady=20)
        result_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        self.result_label = tk.Label(
            result_frame,
            text="Results will appear here",
            font=("Arial", 12),
            bg="#f8f9fa",
            fg="#7f8c8d",
            justify=tk.LEFT,
            wraplength=550
        )
        self.result_label.pack(pady=20, padx=20)
        
        # Focus on input
        self.input_entry.focus()
    
    def calculate(self):
        try:
            user_input = self.input_entry.get().strip()
            if not user_input:
                messagebox.showwarning("Input Required", "Please enter a number!")
                return
            
            number = int(user_input)
            closest_fib, prev2, prev1 = find_closest_fibonacci(number)
            difference = abs(number - closest_fib)
            
            result_text = (
                f"Input number: {number}\n\n"
                f"Closest Fibonacci number: {closest_fib}\n\n"
            )
            
            if closest_fib > 1:
                result_text += f"Formed by: {prev2} + {prev1} = {closest_fib}\n\n"
            
            result_text += f"Difference: {difference}"
            
            self.result_label.config(
                text=result_text,
                font=("Arial", 14),
                fg="#2c3e50"
            )
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer!")
    
    def clear_all(self):
        self.input_entry.delete(0, tk.END)
        self.result_label.config(
            text="Results will appear here",
            font=("Arial", 12),
            fg="#7f8c8d"
        )
        self.input_entry.focus()

def main():
    root = tk.Tk()
    app = FibonacciGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
