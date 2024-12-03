import pyautogui
from datetime import datetime

def clicks_image(image1_path, image2_path):
    # 查找图片在屏幕上的位置
    location1 = pyautogui.locateOnScreen(image1_path) # 左上角
    location2 = pyautogui.locateOnScreen(image2_path) # 右上角

    # 检查是否找到了图片
    if location1 is not None and location2 is not None:
        try:
            # 从位置信息中提取坐标
            left, top, width1, height1 = location1
            right_x, bottom_y, width2, height2 = location2
            
            # 由于locateOnScreen返回的是包含图像的区域，我们需要调整坐标以获取真正的角点
            # 假设图像不是太大，我们可以简单地使用左上角和右下角的坐标
            # 注意：这里我们假设location1是左上角，location2是右下角
            # 在实际应用中，你可能需要根据实际情况调整这部分逻辑
            screenshot_region = (int(left), int(top+height1), int(right_x - left + width2), int(bottom_y - height1 ))
     
            # 截取指定区域
            im = pyautogui.screenshot(region=screenshot_region)
            
            # 使用时间戳保存截图
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"屏幕截图_{timestamp}.png"
            im.save(filename)
            print(f"Screenshot saved as: {filename}")
            
            # 如果需要点击图像位置，可以取消注释以下行
            # pyautogui.click(x + w // 2, y + h // 2)  # 点击图像的中心点
        
        except Exception as e:
            print(f"Image not found on screen: {e}")
    else:
        print("未找到一张或两张图片在屏幕上的位置")

# 调用函数，确保图像路径正确
clicks_image("left.png","right.png")  # 替换为您的图像文件实际路径