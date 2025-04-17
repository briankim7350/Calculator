import tkinter as tk  # Import Tkinter for GUI

# Adds button value to the input
def button_click(value):
    current = display_var.get()  # Get current text
    display_var.set(current + str(value))  # Add new value

# Calculates the result of the expression
def calculate():
    try:
        result = eval(display_var.get())  # Evaluate input
        display_var.set(result)  # Show result
    except ZeroDivisionError:  # Handle divide by 0
        display_var.set("Error")
    except:  # Handle any other error
        display_var.set("Error")

# Clears the input field
def clear():
    display_var.set("")  # Set input to empty

# Create main window
root = tk.Tk()
root.title("Simple Calculator")  # Window title

# Entry box to show input and output
display_var = tk.StringVar()  # Text holder
entry = tk.Entry(root, textvariable=display_var, font=("Times New Roman", 20), justify="right", bd=5)
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Button labels with their positions
btns = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

# Create buttons and place them
for (text, r, c) in btns:
    if text == "=":
        btn = tk.Button(root, text=text, font=("Times New Roman", 16), width=5, height=2, command=calculate)
    else:
        btn = tk.Button(root, text=text, font=("Times New Roman", 16), width=5, height=2, command=lambda val=text: button_click(val))
    btn.grid(row=r, column=c, padx=2, pady=2)

# Create Clear (C) button
clr_btn = tk.Button(root, text="C", font=("Times New Roman", 16), width=23, height=2, command=clear)
clr_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5)

# Start the GUI loop
root.mainloop()
