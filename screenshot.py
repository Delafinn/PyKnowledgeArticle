# How to Guide Script that takes screenshots and helps you take notes.
from pynput import mouse
import pyautogui

SCREENSHOT_COUNTER = 0
COMMENT_COUNTER = 0



def comment():
    # Crestes the comment from the terminal and adds it to the document
    global COMMENT_COUNTER
    usercomment = input('Please notate what step you just performed.')
    with open('HowToGuide.doc','a',encoding="utf-8") as file:
        file.write(f'\n {COMMENT_COUNTER}. {usercomment} \n')
        COMMENT_COUNTER += 1


def capture_screenshot():
    # Counter for numbering screenshots
    global SCREENSHOT_COUNTER

    # Capture screenshot
    filename = f'screenshot{SCREENSHOT_COUNTER}.png'
    pyautogui.screenshot(f'{filename}')
    with open('HowToGuide.doc','a',encoding="utf-8") as file:
        file.write(f' \n Insert {filename} here.')

    # Increment counter for the next screenshot
    SCREENSHOT_COUNTER += 1


def on_click(x, y, button, pressed):
    if pressed:
        capture_screenshot()
        comment()
        print(f"Mouse button {button} pressed at ({x}, {y})")


def main():

    document_title = input("Type in the title of the Knowledge Article:").upper()
    with open('HowToGuide.doc','a',encoding="utf-8") as file:
        file.write(f'{document_title}')

    # Create a mouse listener
    listener = mouse.Listener(on_click=on_click)
    listener.start()

    # Keep the script running
    listener.join()

if __name__ == '__main__':

    main()
