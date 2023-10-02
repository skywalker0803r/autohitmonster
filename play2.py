import pyautogui
import pygetwindow
import time
from PIL import Image

def 切換至目標視窗():
    # 視窗標題或部分標題（不區分大小寫），用來指定特定視窗
    target_window_title = "FairyLand"

    # 取得符合標題的視窗
    target_window = pygetwindow.getWindowsWithTitle(target_window_title)

    # 如果找到了目標視窗
    if target_window:
        target_window = target_window[0]  # 取得第一個符合標題的視窗
        target_window.activate()  # 切換至目標視窗

    else:
        print(f"找不到標題包含 '{target_window_title}' 的視窗。")


def 招怪():
    '''
    判斷是否在戰鬥中若否則持續按壓F7直到進入戰鬥狀態
    '''
    while True:
        # 按下F7键
        pyautogui.keyDown('f7')
        pyautogui.keyUp('f7')
        time.sleep(0.5)  # 等待一秒，给游戏一些时间来响应
        # 在屏幕上查找非戰鬥中的图像
        if pyautogui.locateOnScreen(Image.open('非戰鬥中.PNG')) is None:
            print("招喚怪物成功,正式進入戰鬥")
            break

def 戰鬥():

    # 定义怪物图像文件的路径
    monster_A_path = Image.open('白臭鼬.PNG')
    monster_B_path = Image.open('白鱷魚.PNG')
    monster_C_path = Image.open('黑貓咪.PNG')
    monster_D_path = Image.open('黑鱷魚.PNG')
    
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
        # 搜索怪物D图像
        monster_d_location = pyautogui.locateOnScreen(monster_D_path,confidence=confidence_threshold)

        # 如果找到怪物A图像
        if monster_a_location is not None:
            # 按下黑洞爆發
            pyautogui.keyDown('f6');pyautogui.keyUp('f6')
            time.sleep(0.5) # 等待一段时间，避免连续点击造成问题
            # 点击怪物A图像
            a_x, a_y = pyautogui.center(monster_a_location)
            pyautogui.moveTo(a_x, a_y, 0.5, pyautogui.easeInOutQuad)
            pyautogui.mouseDown(); pyautogui.mouseUp()
            time.sleep(0.5)  # 等待一段时间，避免连续点击造成问题

        # 如果找到怪物B图像
        elif monster_b_location is not None:
            # 按下黑洞爆發
            pyautogui.keyDown('f6');pyautogui.keyUp('f6')
            time.sleep(0.5) # 等待一段时间，避免连续点击造成问题
            # 点击怪物A图像
            b_x, b_y = pyautogui.center(monster_b_location)
            pyautogui.moveTo(b_x, b_y, 0.5, pyautogui.easeInOutQuad)
            pyautogui.mouseDown(); pyautogui.mouseUp()
            time.sleep(0.5)  # 等待一段时间，避免连续点击造成问题

        # 如果找到怪物C图像
        elif monster_c_location is not None:
            # 按下黑洞爆發
            pyautogui.keyDown('f6');pyautogui.keyUp('f6')
            time.sleep(0.5) # 等待一段时间，避免连续点击造成问题
            # 点击怪物A图像
            c_x, c_y = pyautogui.center(monster_c_location)
            pyautogui.moveTo(c_x, c_y, 0.5, pyautogui.easeInOutQuad)
            pyautogui.mouseDown(); pyautogui.mouseUp()
            time.sleep(0.5)  # 等待一段时间，避免连续点击造成问题

        # 如果找到怪物D图像
        elif monster_d_location is not None:
            # 按下黑洞爆發
            pyautogui.keyDown('f6');pyautogui.keyUp('f6')
            time.sleep(0.5) # 等待一段时间，避免连续点击造成问题
            # 点击怪物D图像
            d_x, d_y = pyautogui.center(monster_d_location)
            pyautogui.moveTo(d_x, d_y, 0.5, pyautogui.easeInOutQuad)
            pyautogui.mouseDown(); pyautogui.mouseUp()
            time.sleep(0.5)  # 等待一段时间，避免连续点击造成问题

        else:
            # 如果屏幕上不再出现(A, B, C)怪物图像，退出循环
            print('找不到任何場上怪物')
            break

切換至目標視窗()
time.sleep(0.5)
while True:
    招怪()
    time.sleep(0.5)
    戰鬥()
    time.sleep(0.5)
