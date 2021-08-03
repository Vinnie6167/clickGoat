import pyautogui
import time


def click():
    time.sleep(0.01)
    pyautogui.click()


def move_to_cookie():
    cookie_location = pyautogui.locateCenterOnScreen('images/cookie.png', confidence=0.9)
    if cookie_location is not None:
        pyautogui.moveTo(cookie_location)
        return 0
    else:
        return -1


def main():
    # Move to cookie and click it 20 times
    if move_to_cookie() == 0:
        for i in range(100):
            click()


main()
