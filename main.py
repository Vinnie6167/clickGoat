import pyautogui
import time

assets = ["factory.png", "mine.png", "farm.png", "grandma.png", "cursor.png"]

clicks = 500
buys = 3
upgrades = 3
iterations = 2


# Moves cursor to cookie
def move_to_cookie():
    cookie_location = pyautogui.locateCenterOnScreen('images/cookie.PNG', confidence=0.75)
    if cookie_location is not None:
        pyautogui.moveTo(cookie_location)
        return 0
    else:
        return -1


# Moves cursor to upgrades tile and performs 10 clicks
def upgrade():
    upgrades_location = pyautogui.locateCenterOnScreen('images/store.PNG', confidence=0.9)
    if upgrades_location is not None:
        shift = (-250, 120)
        upgrades_location = upgrades_location + shift
        pyautogui.moveTo(upgrades_location)
        for i in range(10):
            time.sleep(0.01)
            pyautogui.click()
        return 0
    else:
        return -1


# Buys the auto-cookies producers
def buy():
    for asset in assets:
        print(asset)
        asset_location = pyautogui.locateCenterOnScreen('images/' + asset, confidence=0.9)
        if asset_location is not None:
            pyautogui.moveTo(asset_location)
            for i in range(buys):
                time.sleep(0.01)
                pyautogui.click()
        else:
            print(asset + " not found")


def main():
    for i in range(iterations):
        # Move to cookie and click it 20 times
        if move_to_cookie() == 0:
            for i in range(clicks):
                time.sleep(0.01)
                pyautogui.click()

        upgrade()
        buy()


main()
