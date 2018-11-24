import pyautogui
import numpy as np
from PIL import Image
import time

# color rgb 255,219,195 point center light color
# TODO click startbutton
# TODO identify playarea

time.sleep(2)
offset_x = 658
offset_y = 340
# left, top, width, and height
# chrome 100% zoom
while True:
    screen = pyautogui.screenshot(region=(offset_x, offset_y, 605, 408))
    # screen.show()
    im = screen.convert('RGB')
    data = np.array(im)  # "data" is a height x width x 4 numpy array
    r = 0
    g = 1
    b = 2
    r_query = 255
    g_query = 219
    b_query = 195
    a = np.where((data[:, :, r] == r_query) & (
        data[:, :, g] == g_query) & (data[:, :, b] == b_query))
    if a[0].size > 0:
        # TODO optimize targetswitch
        for i in range(0, a[0].size, 250):
            x = offset_x + a[1][i]
            y = offset_y + a[0][i]
            pyautogui.click(x=x, y=y)
    # print(a)
