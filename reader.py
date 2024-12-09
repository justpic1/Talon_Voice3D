
import keyboard
import time


def on_phrase(j):
    print(f"Recognized phrase: {j}")

talon_repl = open(r"c:\Users\Jackson\AppData\Roaming\talon\talon.log")


# Keep the script running
while True:
    try:
        with open(r"c:\Users\Jackson\AppData\Roaming\talon\talon.log") as f:
            lines = f.readlines()
            for line in lines:
                if "Recognized phrase" in line:
                    on_phrase(line)
    except FileNotFoundError:
        print("Talon log file not found. Exiting...")
        break
    try:
        if keyboard.is_pressed("q"):
            print("Exiting...")
            break
    except KeyboardInterrupt:

        pass
    time.sleep(3)
