import time
import pyautogui as pt

pt.FAILSAFE = True


def nav_to_image(image: str, speed: float):
    try:
        pass
        # positions = pt.locateAllOnScreen(image, confidence=.8)
        # pt.moveTo((position[0] / 2) + 10, (position[1] / 2) + 10, duration=speed)  # Mac with Retina display requires division by 2
        # print(positions)
        # pt.doubleClick()

    except Exception as e:
        print(e)
        return 0


def nav_to_reset():
    nav_to_image('restart.png', speed=1)
    pt.doubleClick()


def nav_to_target():
    position = pt.locateCenterOnScreen('circle.png', confidence=.7)
    pt.moveTo((position[0] / 2), (position[1] / 2), duration=0.001)


if __name__ == '__main__':
    for i in range(60):
        nav_to_target()
        print(i)
