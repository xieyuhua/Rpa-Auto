import pyautogui
from datetime import datetime

def clicks_image(path):
    try:
        # 尝试在屏幕上定位图像
        x, y, w, h = pyautogui.locateOnScreen(path)
        print(f"Image found at: x={type(x)}, y={type(y)}, w={type(w)}, h={type(h)}")  # 打印类型以进行调试
        try:
            # 通过2张图片，指定区域截屏 y=y-h x=x      2 x=x+w  y=y

            # 截取指定区域
            im = pyautogui.screenshot(region=(int(x), int(y), w, h))
            # 使用时间戳保存截图
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"屏幕截图_{timestamp}.png"
            im.save(filename)
            print(f"Screenshot saved as: {filename}")
            
            # 如果需要点击图像位置，可以取消注释以下行
            # pyautogui.click(x + w // 2, y + h // 2)  # 点击图像的中心点
        except Exception as e:
            print(f"An error occurred while taking the screenshot: {e}")
    except Exception as e:
        print("Image not found on screen")


# 调用函数，确保图像路径正确
clicks_image("25.png")  # 替换为您的图像文件实际路径
