import pyautogui
from PIL import Image, ImageChops
import time
from PIL import Image

duration_n = 0.8

def 招怪():
    while True:
        print('正在招怪程序')
        # 获取屏幕截图
        screenshot = pyautogui.screenshot()

        # 在屏幕截图中查找图案位置
        img = Image.open('招怪.PNG')
        location = pyautogui.locateOnScreen(img)

        # 如果找到了图案
        if location is not None:
            # 计算图案中心点坐标
            center_x, center_y = pyautogui.center(location)

            # 点击图案中心点
            pyautogui.click(center_x, center_y,duration=duration_n)

            # 等待一段时间，以便观察周围像素的变化（可以根据需要调整等待时间）
            time.sleep(1)

            # 获取新的屏幕截图
            new_screenshot = pyautogui.screenshot()

            # 比较两个截图的不同之处
            diff = ImageChops.difference(screenshot, new_screenshot)

            # 如果有明显的不同（像素不同）
            if diff.getbbox():
                print("跳出招怪程序")
                break


def 戰鬥():

    # 定义怪物图像文件的路径
    monster_A_path = Image.open('怪物圈.PNG')
    monster_B_path = Image.open('怪物圈.PNG')
    monster_C_path = Image.open('怪物圈.PNG')
    黑洞爆發_path = Image.open('黑洞爆發.PNG')
    # 定義模糊比對參數
    confidence_threshold = 0.8

    # 循环直到屏幕上不再出现(A, B, C)怪物图像
    while True:
        # 搜索怪物A图像
        monster_a_location = pyautogui.locateOnScreen(monster_A_path,confidence=confidence_threshold)
        # 搜索怪物B图像
        monster_b_location = pyautogui.locateOnScreen(monster_B_path,confidence=confidence_threshold)
        # 搜索怪物C图像
        monster_c_location = pyautogui.locateOnScreen(monster_C_path,confidence=confidence_threshold)

        # 如果找到怪物A图像
        if monster_a_location is not None:
            # 点击D图像
            d_location = pyautogui.locateOnScreen(黑洞爆發_path,confidence=confidence_threshold)
            if d_location is not None:
                d_x, d_y = pyautogui.center(d_location)
                pyautogui.click(d_x, d_y,duration=duration_n)
                time.sleep(0.5)  # 等待一段时间，避免连续点击造成问题
                # 点击怪物A图像
                a_x, a_y = pyautogui.center(monster_a_location)
                pyautogui.click(a_x, a_y,duration=duration_n)
                time.sleep(0.5)  # 等待一段时间，避免连续点击造成问题

        # 如果找到怪物B图像
        elif monster_b_location is not None:
            # 点击D图像
            d_x, d_y = pyautogui.center(pyautogui.locateOnScreen(黑洞爆發_path,confidence=confidence_threshold))
            pyautogui.click(d_x, d_y,duration=duration_n)
            time.sleep(0.5)  # 等待一段时间，避免连续点击造成问题
            # 点击怪物B图像
            b_x, b_y = pyautogui.center(monster_b_location)
            pyautogui.click(b_x, b_y,duration=duration_n)
            time.sleep(0.5)  # 等待一段时间，避免连续点击造成问题

        # 如果找到怪物C图像
        elif monster_c_location is not None:
            # 点击D图像
            d_x, d_y = pyautogui.center(pyautogui.locateOnScreen(黑洞爆發_path,confidence=confidence_threshold))
            pyautogui.click(d_x, d_y,duration=duration_n)
            time.sleep(0.5)  # 等待一段时间，避免连续点击造成问题
            # 点击怪物C图像
            c_x, c_y = pyautogui.center(monster_c_location)
            pyautogui.click(c_x, c_y,duration=duration_n)
            time.sleep(0.5)  # 等待一段时间，避免连续点击造成问题

        else:
            # 如果屏幕上不再出现(A, B, C)怪物图像，退出循环
            break


while True:
    招怪()
    time.sleep(0.5)
    戰鬥()
    time.sleep(0.5)