# PyKnowledgeArticle
This is a python program that takes inspiration from Tango.us without the AI involvement. But still trying to let users create knowledge articles as fast as possible. 

## How to use

To begin making the how to guide. First make sure to have all the tools you are going to use already up on your monitors. as any RIGHT click you make(while the program is listening)the program will ask you to notate what you just did:

# Warnings!!!

In testing there has been lag on my windows machine after the screenshot is taken and when the program asks you to notate what you just did. I will usually ALT + tab back over to my terminal and make the notatation. After that my windows machine stops lagging and is listening for the next screenshot.
This lag may be specific to my windows device. so let me know if you try this and see lag too. 

Lastly, Adding your screenshots to your ```how to guide.txt``` will need a microsoft office product or I just use google word docs to copy and paste everything into a nice and neat format.
this will be a TODO: in the future to ensure that users don't have to manually build their how to guides.

# To Start

 run:

```sh
python screenshot.py
```

For Mac and Linux users, change the `python` to `python3` for version specification 

You will be prompted to enter the title of the Guide. then you'll be able to start. When you Right click on the screen a full monitor screenshot is taken. (you'll be able to crop the image in google docs or your office product) after the screenshot is taken. reopen the terminal you ran ```python screenshot.py```  It will be prompting you for your notation. ``example : clicked youtube bookmark``




## Installation

1. Clone or download this Github repository
2. Run the following commands to install the dependancies.

```sh
pip install pyautogui
```
```sh
pip install pynput
```

```sh
pip install pillow
```
