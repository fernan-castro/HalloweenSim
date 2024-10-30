"""
    Project: Haunted House GUI
    Team Members: Adriana & Fernando
    Date: 29/10/2024
    Description: A GUI that simulates a haunted house with interactive buttons and sounds.
"""

import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import pygame
import threading
from playsound import playsound

# Function to play sound using pygame
def play_sound(sound_file):
    pygame.mixer.init()  # Initialize the mixer module
    pygame.mixer.music.load(sound_file)  # Load the sound file
    pygame.mixer.music.play()  # Play the sound

# Set up the main window
root = tk.Tk()
root.title("Haunted House Simulator")
root.geometry('500x500')  # Set the window size
root.configure(bg='black')

# Load the Haunted House and Jump Scare images from URLs
haunted_image_url = 'https://i.ibb.co/g4Gh1Pf/Haunted-House.jpg'  # Haunted house URL
jumpscare_image_url = 'https://i.ibb.co/1mQ6d6F/jumpscare.jpg'  # Jump scare URL

try:
    # Load haunted house background image
    response = requests.get(haunted_image_url)
    response.raise_for_status()
    haunted_image = Image.open(BytesIO(response.content))
    haunted_photo = ImageTk.PhotoImage(haunted_image)

    # Load jump scare image
    response = requests.get(jumpscare_image_url)
    response.raise_for_status()
    jumpscare_image = Image.open(BytesIO(response.content))
    jumpscare_photo = ImageTk.PhotoImage(jumpscare_image)

except Exception as e:
    print(f"Error loading images: {e}")
    haunted_photo, jumpscare_photo = None, None

# Display haunted house image if it loaded successfully
canvas = tk.Canvas(root, bg='black')
canvas.pack(fill='both', expand=True)

if haunted_photo:
    canvas.create_image(0, 0, anchor='nw', image=haunted_photo)

# Function for the jump scare
def jump_scare():
    # Hide buttons
    enter_button.place_forget()
    leave_button.place_forget()
    
    # Display the jump scare image
    canvas.create_image(0, 0, anchor='nw', image=jumpscare_photo)
    
    # Play creepy sound effect in a separate thread
    sound_thread = threading.Thread(target=play_sound, args=('SFX/jumpscare.mp3',))
    sound_thread.start()

    # Close the program after a brief delay (1000 ms = 1 second)
    root.after(1000, root.destroy)  # This will exit the program after 1 second

# Function to enter the house
def enter_house():
    enter_button.place_forget()
    leave_button.place_forget()
    # Additional code for exploring the house can be added here

# Function to turn around and leave
def turn_around_and_leave():
    jump_scare()  # Trigger the jump scare

def play_creepy_sound():
    threading.Thread(target=lambda: playsound('SFX/creppy_sound.mp3')).start()

# Create initial buttons
enter_button = tk.Button(root, text="Enter the house", command=enter_house, bg='grey', fg='black')
enter_button.place(relx=0.5, rely=0.8, anchor='center')  # Centered near the bottom

leave_button = tk.Button(root, text="Turn around and leave", command=turn_around_and_leave, bg='grey', fg='black')
leave_button.place(relx=0.5, rely=0.9, anchor='center')  # Centered below "Enter the house" button

play_creepy_sound()

# Start the GUI loop
root.mainloop()
