from pynput import mouse
import pyautogui

screenshot_counter = 0
comment_counter = 0



def comment():
    global comment_counter
    usercomment = input('Please notate what step you just performed.')
    with open('HowToGuide.doc','a') as file:
        file.write(f'\n {comment_counter}. {usercomment} \n')
        comment_counter += 1


def capture_screenshot():
    # Counter for numbering screenshots
    global screenshot_counter

    # Capture screenshot
    filename = f'screenshot{screenshot_counter}.png'
    screenshot = pyautogui.screenshot(f'{filename}')
    with open('HowToGuide.doc','a') as file:
        file.write(f' \n Insert {filename} here.')

    # Increment counter for the next screenshot
    screenshot_counter += 1



def on_click(x, y, button, pressed):
    if pressed:
        capture_screenshot()
        comment()
        print(f"Mouse button {button} pressed at ({x}, {y})")



def main():

    document_title = input("Type in the title of the Knowledge Article:").upper()
    with open('HowToGuide.doc','a') as file:
        file.write(f'{document_title}')

    # Create a mouse listener
    listener = mouse.Listener(on_click=on_click)
    listener.start()

    # Keep the script running
    listener.join()


main()
