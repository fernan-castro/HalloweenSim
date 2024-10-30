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

# Load the Haunted House, Jump Scare, and Interior images from URLs
haunted_image_url = 'https://i.ibb.co/g4Gh1Pf/Haunted-House.jpg'  # Haunted house URL
jumpscare_image_url = 'https://i.ibb.co/1mQ6d6F/jumpscare.jpg'  # Jump scare URL
interior_image_url = 'https://i.ibb.co/x1PndDS/Interior.jpg'  # Interior URL

def load_image(url):
    """Helper function to load an image from a URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content)).resize((500, 500), Image.LANCZOS)  # Updated from ANTIALIAS to LANCZOS
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error loading image from {url}: {e}")
        return None

# Load images
haunted_photo = load_image(haunted_image_url)
jumpscare_photo = load_image(jumpscare_image_url)
interior_photo = load_image(interior_image_url)

# Create a canvas that fills the entire window
canvas = tk.Canvas(root, bg='black', width=500, height=500)
canvas.pack(fill='both', expand=True)

# Keep references to the images to prevent garbage collection
canvas.image_haunted = haunted_photo
canvas.image_jumpscare = jumpscare_photo
canvas.image_interior = interior_photo

# Display haunted house image if it loaded successfully
if haunted_photo:
    canvas.create_image(0, 0, anchor='nw', image=haunted_photo)
else:
    print("Haunted house image failed to load.")

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

# Function to enter the house (pitch black)
def enter_house():
    enter_button.place_forget()
    leave_button.place_forget()
    
    # Clear the canvas and make it pitch black
    canvas.create_rectangle(0, 0, 500, 500, fill='black')
    
    # Create options for the dark room
    dark_label = tk.Label(root, text="It's pitch black! What do you want to do?", font=("Helvetica", 16), fg='white', bg='black')
    dark_label.place(relx=0.5, rely=0.4, anchor='center')

    turn_on_lights_button = tk.Button(root, text="Turn on Lights", command=turn_on_lights, bg='grey', fg='black')
    turn_on_lights_button.place(relx=0.5, rely=0.6, anchor='center')

    leave_dark_room_button = tk.Button(root, text="Leave", command=jump_scare, bg='grey', fg='black')
    leave_dark_room_button.place(relx=0.5, rely=0.7, anchor='center')

# Function to turn on the lights
def turn_on_lights():
    # Clear the canvas and show the interior image
    canvas.create_image(0, 0, anchor='nw', image=interior_photo)  # Display the interior image
    lights_label = tk.Label(root, text="The lights are on! You're safe for now.", font=("Helvetica", 16), fg='black', bg='white')
    lights_label.place(relx=0.5, rely=0.4, anchor='center')

    # Option to leave the room
    leave_button = tk.Button(root, text="Leave the House", command=jump_scare, bg='grey', fg='black')
    leave_button.place(relx=0.5, rely=0.6, anchor='center')

def play_creepy_sound():
    threading.Thread(target=lambda: playsound('SFX/creppy_sound.mp3')).start()

# Create initial buttons
enter_button = tk.Button(root, text="Enter the house", command=enter_house, bg='grey', fg='black')
enter_button.place(relx=0.5, rely=0.8, anchor='center')  # Centered near the bottom

leave_button = tk.Button(root, text="Turn around and leave", command=jump_scare, bg='grey', fg='black')
leave_button.place(relx=0.5, rely=0.9, anchor='center')  # Centered below "Enter the house" button

play_creepy_sound()

# Start the GUI loop
root.mainloop()
