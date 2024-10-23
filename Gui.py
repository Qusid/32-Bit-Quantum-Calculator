from Upto32BitAdder import Adder
from Upto32BitMultiplier import Multiply
from Upto32Subtractor import Sub
import tkinter as tk
from tkinter import messagebox

# GUI Application
class QuantumCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quantum Calculator")
        self.root.geometry("400x350")
        self.operation = tk.StringVar(value="add")
        self.circuit = None  # Store the quantum circuit

        # Create widgets
        self.create_widgets()

    def create_widgets(self):
        # Number Entry Fields
        tk.Label(self.root, text="First Number:").pack(pady=5)
        self.num1_entry = tk.Entry(self.root)
        self.num1_entry.pack(pady=5)

        tk.Label(self.root, text="Second Number:").pack(pady=5)
        self.num2_entry = tk.Entry(self.root)
        self.num2_entry.pack(pady=5)

        # Operation Selection
        tk.Label(self.root, text="Select Operation:").pack(pady=5)
        operations_frame = tk.Frame(self.root)
        operations_frame.pack(pady=5)

        tk.Radiobutton(operations_frame, text="Add", variable=self.operation, value="add").pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(operations_frame, text="Subtract", variable=self.operation, value="subtract").pack(side=tk.LEFT, padx=5)
        tk.Radiobutton(operations_frame, text="Multiply", variable=self.operation, value="multiply").pack(side=tk.LEFT, padx=5)

        # Calculate Button
        tk.Button(self.root, text="Calculate", command=self.calculate).pack(pady=10)

        # Show Circuit Button
        self.show_circuit_button = tk.Button(self.root, text="Show Circuit", command=self.show_circuit)
        self.show_circuit_button.pack(pady=5)
        self.show_circuit_button.config(state=tk.DISABLED)  # Disable until calculation is done

        # Result Label
        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def calculate(self):
        num1 = self.num1_entry.get()
        num2 = self.num2_entry.get()
        operation = self.operation.get()

        try:
            a = int(num1)
            b = int(num2)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid integers.")
            return

        if operation == "add":
            result, qc = Adder(a, b)
            operation_symbol = '+'
        elif operation == "subtract":
            result, qc = Sub(a, b)
            operation_symbol = '-'
        elif operation == "multiply":
            result, qc = Multiply(a, b)
            operation_symbol = '*'
        else:
            messagebox.showerror("Invalid Operation", "Please select a valid operation.")
            return

        self.circuit = qc  # Store the circuit
        self.show_circuit_button.config(state=tk.NORMAL)  # Enable the button
        self.result_label.config(text=f"{a} {operation_symbol} {b} = {result}")

    def show_circuit(self):
        if self.circuit is None:
            messagebox.showinfo("No Circuit", "No circuit to display.")
            return

        # Create a new window to display the circuit
        circuit_window = tk.Toplevel(self.root)
        circuit_window.title("Quantum Circuit")

        # Convert the circuit to a text drawing
        circuit_text = self.circuit.draw(output='text')

        # Create a Text widget to display the circuit
        text_widget = tk.Text(circuit_window, wrap='none', font=('Courier', 10))
        text_widget.insert('1.0', circuit_text)
        text_widget.configure(state='disabled')  # Make it read-only
        text_widget.pack(expand=True, fill='both')

        # Add scrollbars
        x_scroll = tk.Scrollbar(circuit_window, orient='horizontal', command=text_widget.xview)
        x_scroll.pack(side='bottom', fill='x')
        y_scroll = tk.Scrollbar(circuit_window, orient='vertical', command=text_widget.yview)
        y_scroll.pack(side='right', fill='y')
        text_widget.configure(xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = QuantumCalculatorApp(root)
    root.mainloop()