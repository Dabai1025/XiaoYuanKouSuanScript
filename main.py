import pytesseract
import pyautogui
import cv2
import numpy as np
import os
import time

script_dir = os.path.dirname(__file__) # 获取当前脚本所在路径
defaultX = 175
defaultY = 710
addSize = 50

def moveMouseBigger():
    pyautogui.mouseDown(defaultX,defaultY)
    pyautogui.moveTo(defaultX+addSize, defaultY+addSize, duration=0.1)
    pyautogui.moveTo(defaultX, defaultY+addSize, duration=0.1)
    pyautogui.mouseUp()

def moveMouseSmaller():
    pyautogui.mouseDown(defaultX,defaultY)
    pyautogui.moveTo(defaultX-addSize, defaultY+addSize, duration=0.1)
    pyautogui.moveTo(defaultX, defaultY+addSize, duration=0.1)
    pyautogui.mouseUp()
    
def getScreen():
    img = pyautogui.screenshot(region=[3,45, 449,1038]) # 对屏幕截图，位置为绝对位置
    img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR) # 将颜色空间 RGB 转换成 BGR 便于后续 cv2 库进行处理
    cv2.imwrite(script_dir + "\\screenLeftOutput.png", img[250:307, 120:200, 1]) # 裁剪并输出图像文件
    cv2.imwrite(script_dir + "\\screenRightOutput.png", img[250:307, 250:330, 1]) # 裁剪并输出图像文件
    LeftImgPath = script_dir + "\\screenLeftOutput.png"
    RightImgPath = script_dir + "\\screenRightOutput.png"
    return LeftImgPath, RightImgPath

while(1):

    LeftImgPath, RightImgPath = getScreen()
    textLeft = pytesseract.image_to_string(LeftImgPath, lang="eng", config="--psm 6")
    textRight = pytesseract.image_to_string(RightImgPath, lang="eng", config="--psm 6")

    if (int(textLeft)>int(textRight)):
        print("左边的数字是: " + textLeft)
        print("右边的数字是: " + textRight)
        print("左边的数字大")
        moveMouseBigger()
        time.sleep(0.5)
        
    else:
        print("左边的数字是 v: " + textLeft)
        print("右边的数字是: " + textRight)
        print("右边的数字大")
        moveMouseSmaller()
        time.sleep(0.5)
        

