import tkinter as tk
import re


class RealTimeCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-Time Calculator")
        self.root.configure(bg="#f0f0f0")
        self.root.geometry("400x300")

        # Expression variables
        self.current_expression = ""
        self.current_result = ""

        # Create the main display frame
        display_frame = tk.Frame(root, bg="#f0f0f0")
        display_frame.pack(pady=10)

        # Label for expression
        self.expression_var = tk.StringVar()
        self.expression_label = tk.Label(
            display_frame,
            textvariable=self.expression_var,
            font=("Arial", 14),
            anchor="e",
            bg="#f0f0f0",
            width=25
        )
        self.expression_label.pack(pady=5)

        # Label for real-time result
        self.result_var = tk.StringVar()
        self.result_var.set("0")
        self.result_label = tk.Label(
            display_frame,
            textvariable=self.result_var,
            font=("Arial", 20, "bold"),
            anchor="e",
            bg="white",
            relief="sunken",
            width=20,
            height=2
        )
        self.result_label.pack(pady=5)

        # Create entry widget for input
        self.entry = tk.Entry(
            root,
            font=("Arial", 16),
            justify="right",
            bd=5
        )
        self.entry.pack(pady=10, padx=20, fill=tk.X)
        self.entry.bind("<KeyRelease>", self.calculate_on_type)
        self.entry.focus_set()

        # Button to clear input
        clear_button = tk.Button(
            root,
            text="Clear",
            font=("Arial", 12),
            command=self.clear_input,
            bg="#ff6b6b",
            fg="white",
            bd=3,
            relief=tk.RAISED,
            padx=20,
            pady=10
        )
        clear_button.pack(pady=10)

    def calculate_on_type(self, event):
        """Calculate the result in real-time as the user types"""
        self.current_expression = self.entry.get()
        self.expression_var.set(self.current_expression)

        if not self.current_expression:
            self.result_var.set("0")
            return

        try:
            # Prepare the expression for evaluation
            expression = self.prepare_expression(self.current_expression)

            # Safely evaluate the expression
            result = eval(expression)

            # Format result based on whether it's an integer or float
            if result == int(result):
                self.result_var.set(str(int(result)))
            else:
                self.result_var.set(
                    str(round(result, 8)).rstrip('0').rstrip('.') if '.' in str(result) else str(result))

        except Exception as e:
            # If expression is incomplete or invalid, just show the current input
            # This handles cases like "5+" where we want to show 5 until another operand is entered
            try:
                # Try to evaluate the expression up to the last complete operation
                last_number = re.search(r"[\d.]+$", self.current_expression)
                if last_number:
                    # Just display the last complete number if there's no complete operation
                    self.result_var.set(last_number.group())
                else:
                    # Find the last valid expression result
                    partial_expr = re.sub(r"[+\-*/]$", "", self.current_expression)
                    if partial_expr:
                        partial_result = eval(self.prepare_expression(partial_expr))
                        if partial_result == int(partial_result):
                            self.result_var.set(str(int(partial_result)))
                        else:
                            self.result_var.set(str(round(partial_result, 8)).rstrip('0').rstrip('.'))
                    else:
                        self.result_var.set("0")
            except:
                # If all fails, just use the input as is
                self.result_var.set(self.current_expression)

    def prepare_expression(self, expr):
        """Prepare the expression for safe evaluation"""
        # Handle expressions that start with a negative number
        expr = expr.replace("×", "*").replace("÷", "/")
        return expr

    def clear_input(self):
        """Clear the input field"""
        self.entry.delete(0, tk.END)
        self.current_expression = ""
        self.expression_var.set("")
        self.result_var.set("0")
        self.entry.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    app = RealTimeCalculator(root)
    root.mainloop()