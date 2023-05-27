# How to Guide Script that takes screenshots and helps you take notes.
from pynput import mouse
import pyautogui
from record_comment import *




def on_click(x, y, button, pressed):
    if button == mouse.Button.right and pressed:
        print(f"Mouse button {button} pressed at ({x}, {y})")
        # Counter for numbering screenshots
        SCREENSHOT_COUNTER = 0

        # Capture screenshot
        filename = f'screenshot{SCREENSHOT_COUNTER}.png'
        pyautogui.screenshot(f'{filename}',region =(x,y,240,480))
        with open('HowToGuide.doc','a') as file:
            file.write(f' \n Insert {filename} here.')

        # Increment counter for the next screenshot
        SCREENSHOT_COUNTER += 1
        record_com()





def main():

    document_title = input("Type in the title of the Knowledge Article:").upper()
    with open('HowToGuide.doc','a') as file:
        file.write(f'{document_title}')

    # Create a mouse listener
    listener = mouse.Listener(on_click=on_click)
    listener.start()

    # Keep the script running
    listener.join()






if __name__ == '__main__':

    main()
