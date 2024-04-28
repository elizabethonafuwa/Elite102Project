import tkinter as tk

def show_welcome_screen():
    welcome_window = tk.Tk()
    welcome_window.title("Welcome")
    welcome_label = tk.Label(welcome_window, text="Welcome to Online Banking System!")
    welcome_label.pack(padx=20, pady=20)
    close_button = tk.Button(welcome_window, text="Close", command=welcome_window.destroy)
    close_button.pack(pady=10)

# Create the main window
root = tk.Tk()
root.title("Online Banking System")

# Create a welcome button
welcome_button = tk.Button(root, text="Welcome", command=show_welcome_screen)
welcome_button.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
