import tkinter as tk
from tkinter import scrolledtext, messagebox

def kaprekar_routine(num):
    """
    Perform one iteration of the Kaprekar routine.
    Returns the result of: (largest arrangement - smallest arrangement)
    """
    # Convert to 4-digit string with leading zeros if needed
    digits = str(num).zfill(4)
    
    # Sort digits in descending order (largest)
    largest = int(''.join(sorted(digits, reverse=True)))
    
    # Sort digits in ascending order (smallest)
    smallest = int(''.join(sorted(digits)))
    
    # Subtract
    result = largest - smallest
    
    return result, largest, smallest

def kaprekar_constant(num, output_widget):
    """
    Demonstrate Kaprekar's constant (6174) by repeatedly applying the routine.
    """
    KAPREKAR_CONSTANT = 6174
    
    # Clear previous output
    output_widget.config(state=tk.NORMAL)
    output_widget.delete(1.0, tk.END)
    
    # Validate input
    if num < 0 or num > 9999:
        output_widget.insert(tk.END, "❌ Error: Number must be between 0 and 9999\n", "error")
        output_widget.config(state=tk.DISABLED)
        return None
    
    # Check if all digits are the same (these don't work)
    digits = str(num).zfill(4)
    if len(set(digits)) == 1:
        output_widget.insert(tk.END, "❌ Error: Number must have at least two different digits\n", "error")
        output_widget.config(state=tk.DISABLED)
        return None
    
    current = num
    
    output_widget.insert(tk.END, f"Starting number: {num}\n", "header")
    output_widget.insert(tk.END, "-" * 60 + "\n\n", "separator")
    
    step = 0
    while current != KAPREKAR_CONSTANT and step < 10:
        result, largest, smallest = kaprekar_routine(current)
        step += 1
        
        output_widget.insert(tk.END, f"Step {step}: ", "step")
        output_widget.insert(tk.END, f"{largest} - {smallest} = {result}\n", "normal")
        
        current = result
        
        # Check if we've reached the constant
        if current == KAPREKAR_CONSTANT:
            output_widget.insert(tk.END, f"\n✓ Reached Kaprekar's constant {KAPREKAR_CONSTANT} in {step} steps!\n", "success")
            output_widget.config(state=tk.DISABLED)
            return True
    
    if current == KAPREKAR_CONSTANT:
        output_widget.config(state=tk.DISABLED)
        return True
    else:
        output_widget.insert(tk.END, "\n❌ Did not converge\n", "error")
        output_widget.config(state=tk.DISABLED)
        return False

class KaprekarGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Kaprekar's Constant (6174)")
        self.root.geometry("700x600")
        self.root.resizable(True, True)
        
        # Title Frame
        title_frame = tk.Frame(root, bg="#2c3e50", pady=15)
        title_frame.pack(fill=tk.X)
        
        title_label = tk.Label(
            title_frame, 
            text="KAPREKAR'S CONSTANT (6174)", 
            font=("Arial", 18, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        title_label.pack()
        
        # Info Frame
        info_frame = tk.Frame(root, bg="#ecf0f1", pady=10)
        info_frame.pack(fill=tk.X, padx=10, pady=10)
        
        info_text = (
            "The Kaprekar Routine:\n"
            "1. Take a 4-digit number (with at least 2 different digits)\n"
            "2. Arrange digits in descending order\n"
            "3. Arrange digits in ascending order\n"
            "4. Subtract the smaller from the larger\n"
            "5. Repeat with the result\n"
            "6. You'll always reach 6174!"
        )
        
        info_label = tk.Label(
            info_frame,
            text=info_text,
            font=("Arial", 10),
            bg="#ecf0f1",
            justify=tk.LEFT
        )
        info_label.pack(padx=10)
        
        # Input Frame
        input_frame = tk.Frame(root, pady=10)
        input_frame.pack(fill=tk.X, padx=10)
        
        input_label = tk.Label(
            input_frame,
            text="Enter a number (0-9999):",
            font=("Arial", 12)
        )
        input_label.pack(side=tk.LEFT, padx=5)
        
        self.input_entry = tk.Entry(
            input_frame,
            font=("Arial", 12),
            width=15
        )
        self.input_entry.pack(side=tk.LEFT, padx=5)
        self.input_entry.bind('<Return>', lambda e: self.calculate())
        
        calc_button = tk.Button(
            input_frame,
            text="Calculate",
            font=("Arial", 12, "bold"),
            bg="#3498db",
            fg="white",
            command=self.calculate,
            padx=20
        )
        calc_button.pack(side=tk.LEFT, padx=5)
        
        clear_button = tk.Button(
            input_frame,
            text="Clear",
            font=("Arial", 12),
            bg="#95a5a6",
            fg="white",
            command=self.clear_output,
            padx=20
        )
        clear_button.pack(side=tk.LEFT, padx=5)
        
        # Output Frame
        output_frame = tk.Frame(root)
        output_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        output_label = tk.Label(
            output_frame,
            text="Results:",
            font=("Arial", 12, "bold")
        )
        output_label.pack(anchor=tk.W, pady=(0, 5))
        
        self.output_text = scrolledtext.ScrolledText(
            output_frame,
            font=("Consolas", 11),
            wrap=tk.WORD,
            height=15,
            bg="#f9f9f9"
        )
        self.output_text.pack(fill=tk.BOTH, expand=True)
        
        # Configure text tags for styling
        self.output_text.tag_config("header", font=("Consolas", 11, "bold"), foreground="#2c3e50")
        self.output_text.tag_config("separator", foreground="#7f8c8d")
        self.output_text.tag_config("step", font=("Consolas", 11, "bold"), foreground="#16a085")
        self.output_text.tag_config("normal", foreground="#34495e")
        self.output_text.tag_config("success", font=("Consolas", 11, "bold"), foreground="#27ae60")
        self.output_text.tag_config("error", font=("Consolas", 11, "bold"), foreground="#e74c3c")
        
        self.output_text.config(state=tk.DISABLED)
        
        # Focus on input
        self.input_entry.focus()
    
    def calculate(self):
        try:
            user_input = self.input_entry.get().strip()
            if not user_input:
                messagebox.showwarning("Input Required", "Please enter a number!")
                return
            
            number = int(user_input)
            kaprekar_constant(number, self.output_text)
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer!")
    
    def clear_output(self):
        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete(1.0, tk.END)
        self.output_text.config(state=tk.DISABLED)
        self.input_entry.delete(0, tk.END)
        self.input_entry.focus()

def main():
    root = tk.Tk()
    app = KaprekarGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
