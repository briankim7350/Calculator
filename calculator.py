import tkinter as tk

# Function to update input field
def on_button_click(value):
    entry_var.set(entry_var.get() + str(value))

# Function to evaluate expression
def calculate():
    try:
        entry_var.set(eval(entry_var.get()))  # Evaluate the expression
    except ZeroDivisionError:
        entry_var.set("Error")
    except:
        entry_var.set("Error")

# Function to clear input field
def clear():
    entry_var.set("")

# Create main window
root = tk.Tk()
root.title("Simple Calculator")

# Create input field
entry_var = tk.StringVar()
entry = tk.Entry(root, textvariable=entry_var)
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Create buttons
for text, row, col in buttons:
    button = tk.Button(root, text=text, command=(calculate if text == "=" else lambda t=text: on_button_click(t)))
    button.grid(row=row, column=col)

# Clear button
clear_button = tk.Button(root, text="C", command=clear)
clear_button.grid(row=5, column=0, columnspan=4)

# Run the GUI
root.mainloop()
