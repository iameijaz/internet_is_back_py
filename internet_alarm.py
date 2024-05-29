import tkinter as tk
from tkinter import messagebox
import requests
import time
import threading
from playsound import playsound
from tkinter import ttk
from speedtest import Speedtest

# Flag to control internet checking thread
checking_internet = True

def is_connected():
    try:
        requests.get('https://www.google.com/', timeout=2)
        return True
    except requests.ConnectionError:
        return False

def check_internet():
    global checking_internet
    while checking_internet:
        if is_connected():
            status_label.config(text="Status: Connected", fg="green")
            if play_sound_var.get():
                playsound('sound.mp3')
                messagebox.showinfo("Internet is back", "Internet connection is restored!")
            break
        else:
            status_label.config(text="Status: Checking...", fg="orange")
        time.sleep(2)

def measure_speed():
    global checking_internet
    # Pause the internet checking
    checking_internet = False
    status_label.config(text="Status: Measuring Speed...", fg="blue")
    st = Speedtest()
    download_speed = st.download()
    upload_speed = st.upload()
    messagebox.showinfo("Internet Speed", f"Download Speed: {download_speed / 10**6:.2f} Mbps\nUpload Speed: {upload_speed / 10**6:.2f} Mbps")
    status_label.config(text="Status: Not Connected", fg="red")
    # Resume the internet checking
    checking_internet = True
    start_checking()

def start_checking():
    threading.Thread(target=check_internet, daemon=True).start()

# Create main window
window = tk.Tk()
window.title("Internet Checker")

# Create and configure label
status_label = tk.Label(window, text="Status: Not Connected", fg="red")
status_label.pack(pady=10)

# Checkbox to choose whether to play sound or not
play_sound_var = tk.BooleanVar()
play_sound_var.set(True)
play_sound_checkbox = tk.Checkbutton(window, text="Play sound when internet is available", variable=play_sound_var)
play_sound_checkbox.pack()

# Button to measure internet speed
speed_button = ttk.Button(window, text="Measure Internet Speed", command=lambda: threading.Thread(target=measure_speed, daemon=True).start())
speed_button.pack(pady=5)

# Start checking for internet as soon as the app runs
start_checking()

# Run the application
window.mainloop()
