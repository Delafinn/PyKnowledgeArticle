import sys


def continuequestion():
    from pynput import mouse
    cq = input('Do you wish to continue with the guide?')
    if cq in ('no','n'):
        try:
            listener.stop()

        except NotImplementedError():
            print('oops! ran into a problem')


        else:
            listener.stop()
            sys.exit()

    else:
        pass


def record_com():
    # Crestes the comment from the terminal and adds it to the document
    COMMENT_COUNTER = 0
    usercomment = input('Please notate what step you just performed.')
    with open('HowToGuide.doc','a') as file:
        file.write(f'\n {COMMENT_COUNTER}. {usercomment} \n')
        COMMENT_COUNTER += 1
        continuequestion()
