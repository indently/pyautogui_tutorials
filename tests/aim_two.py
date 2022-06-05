import pyautogui as pag
# On Mac you get double the pixels, so you need to use /2

def move_to_location(image):
    position = pag.locateCenterOnScreen(image, confidence=0.7)
    x = position[0] / 2
    y = position[1] / 2
    pag.moveTo(x, y, duration=0.1)
    print(x, y)

    return [x, y]


def find_window_region():
    top_left = move_to_location('top_left_window.png')
    bottom_right = move_to_location('bottom_right_window.png')

    window = (bottom_right[0] + top_left[0], bottom_right[1] + top_left[1])
    print(window)
    pag.moveTo(window[0] / 2, window[1] / 2, duration=1)


if __name__ == '__main__':
    find_window_region()

# RGB(red=55, green=121, blue=200)
