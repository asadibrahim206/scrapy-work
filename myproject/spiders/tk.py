import tkinter as tk

def greet():
    name = entry.get() # Get text from the entry box
    greeting_label.config(text=f"Hello, {name}!")

root = tk.Tk()
root.title("Greeter")

# UI Elements
tk.Label(root, text="Enter your name:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

greet_button = tk.Button(root, text="Greet Me", command=greet)
greet_button.grid(row=1, column=0, columnspan=2, pady=10)

greeting_label = tk.Label(root, text="")
greeting_label.grid(row=2, column=0, columnspan=2)

root.mainloop()