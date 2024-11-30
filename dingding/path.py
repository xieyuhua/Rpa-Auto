from pywinauto import Desktop
# from pywinauto import keyboard
import time
import pyautogui
import keyboard  # 你需要安装keyboard库：pip install keyboard
from pywinauto.keyboard import *
import pyperclip

# 唤醒钉钉窗口，指定窗口位置，识别文字，包含文字（###），发布消息（###）enter
# pip install --upgrade pyautogui pyscreeze

# 查找钉钉窗口（这里需要根据你的实际情况调整窗口标题或类名）
dingding_window = Desktop(backend="uia").window(title_re=".*钉钉.*")

def click_image(path):
    xy = pyautogui.locateOnScreen(path)
    if xy:
        center = pyautogui.center(xy)
        pyautogui.click(center)
        print("Clicked on the image.")
    else:
        print("Image not found.")

# 确保窗口存在并且是可见的
if dingding_window.exists() and dingding_window.is_visible():
    dingding_window.set_focus()
    print("找到钉钉窗口")
else:
    print("未找到钉钉窗口")

# 原始字符串
original_string = ""
 
while True:
    try:
        # chatbox_window.set_focus()
        dingding_window.set_focus()
        click_image('1.png')
        
        send_keys('^a')
        # time.sleep(0.5)  # 等待片刻以确保全选操作完成
        send_keys('^c')

        # pyperclip.copy("")
        # 获取剪贴板上的文本
        clipboard_text = pyperclip.paste()
        # 打印剪贴板上的文本

        new_string = clipboard_text.replace(original_string, "")
        # 输出替换后的字符串
        print("最新数据：", new_string)

        original_string = clipboard_text
        # exit()
        reply_text = "收到"
    
        # dingding_window.set_focus()
        time.sleep(0.1)
        click_image('4.png')


        # 定义两个字符串  new_string
        main_string = "Hello, world!"
        sub_string = "world"
        
        # 使用in关键字判断main_string是否包含sub_string
        if sub_string in main_string:
            keyboard.write(reply_text)
            keyboard.press_and_release('enter')  # 发送消息
            print(f"'{main_string}' 包含 '{sub_string}'")
        else:
            print(f"'{main_string}' 不包含 '{sub_string}'")

        time.sleep(1)
    except Exception as e:
        print("Failed :", e)
