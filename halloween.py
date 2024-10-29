"""
    Project: Haunted House GUI
    Team Members:
    Date:
    Description: A GUI that simulates a haunted house with interactive buttons and sounds.
"""

import tkinter as tk


# Set up the main window
root = tk.Tk()
root.title("Haunted House Simulator")

# Create widgets
label = tk.Label(root, text="Welcome to the Haunted House!", font=("Helvetica", 16))
label.pack(pady=20)



# Start the GUI loop
root.mainloop()