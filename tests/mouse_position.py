import pyautogui as pt
from time import sleep


if __name__ == '__main__':
    while True:
        pos = pt.position()
        color = pt.pixel(pos[0], pos[1])
        print(pos)
        print(color)
        sleep(2)
