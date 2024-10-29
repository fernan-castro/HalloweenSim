"""
    Project: Haunted House GUI
    Team Members: Adriana & Fernando
    Date: 29/10/2024
    Description: A GUI that simulates a haunted house with interactive buttons and sounds.
"""

import tkinter as tk
from playsound import playsound


# Set up the main window
root = tk.Tk()
root.title("Haunted House Simulator")
root.geometry("800x600")
root.configure(bg="black")

# Create widgets
label = tk.Label(root, text="Welcome to the Haunted House!", font=("Helvetica", 16))
label.pack(pady=20)

# Function to turn on lights
def turn_on_lights():
    label.config(text="The lights are on!")

# Function to play creepy sound
def play_creepy_sound():
    playsound('SFX/creppy_sound.mp3')

# Function to open door
def open_door():
    label.config(text="The door creaks open...")

# Create buttons
light_button = tk.Button(root, text="Turn on Lights", command=turn_on_lights)
light_button.pack(pady=10)

sound_button = tk.Button(root, text="Play Creepy Sound", command=play_creepy_sound)
sound_button.pack(pady=10)

door_button = tk.Button(root, text="Open Door", command=open_door)
door_button.pack(pady=10)

# Start the GUI loop
root.mainloop()