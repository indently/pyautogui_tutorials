import pyautogui as pag
# pip install opencv-python to use the 'confidence' parameter

pag.FAILSAFE = True
# pag.PAUSE = 1


def get_position(image: str):
    try:
        position = pag.locateCenterOnScreen(image, confidence=0.8)
        if position is None:
            print(f'{image} not found on screen...')
            return None
        else:
            # On Mac you get double the pixels, so you need to divide / 2
            x = position[0] / 2
            y = position[1] / 2
            # print(x, y)
            return x, y
    except OSError as e:
        raise Exception(e)


def drag_to_target(image: str, target: str, speed: float):
    position = get_position(image)
    target = get_position(target)

    if None not in [position, target]:
        pag.moveTo(position, duration=speed)
        pag.dragTo(target, button='left', duration=speed)
    else:
        raise Exception('Could not complete the request, because one of the images returned None.')


def main():
    # In general, try to avoid using infinite loops in programs that control your gui
    while True:
        drag_to_target(image='target_file.png', target='target_folder.png', speed=0.5)


if __name__ == '__main__':
    main()

