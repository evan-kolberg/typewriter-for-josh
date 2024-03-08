import keyboard
import random as r
from pynput.keyboard import Key, Listener
import time

text = ''

reversed_keyboard_dict = {
    'e': 0.07, 't': 0.10, 'a': 0.11, 'o': 0.17, 'i': 0.69, 'n': 0.10, 's': 0.11, 'r': 0.17, 'h': 0.92,
    'd': 0.69, 'l': 0.98, 'u': 1.88, 'c': 1.71, 'm': 1.61, 'f': 2.30, 'y': 2.11, 'w': 2.09, 'g': 2.03,
    'p': 1.82, 'b': 1.49, 'v': 1.11, 'k': 4.32, 'x': 5.02, 'q': 6.28, 'j': 6.31, 'z': 14.02
}

def run(input_text):
    for i in input_text.split():
        for j in i:
            if i.isalnum() == False:
                if r.randint(0,20) <= 1:
                    time.sleep(r.uniform(0.4, 2.2) * reversed_keyboard_dict.get(j, 1))
                else:
                    time.sleep(r.uniform(0.32, 0.81) * reversed_keyboard_dict.get(j, 1))
            else:
                time.sleep(r.uniform(0.23, 1.335) * reversed_keyboard_dict.get(j, 1))
            keyboard.write(j)
            print(f'\033[32mSent key "{j}"\033[31m')
        time.sleep(r.uniform(0, 1))
        keyboard.send(' ')

if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        text = file.read()

    def on_press(key):
        if key == Key.shift:
            print(f"\n\033[32mRunning...\033[31m\n")
            run(text)
            print(f"\n\033[32mDone!\033[31m")

    with Listener(on_press=on_press) as listener:
        listener.join()


