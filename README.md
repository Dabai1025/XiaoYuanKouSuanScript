# XiaoYuanKouSuanScript
## 小猿口算比大小辅助脚本

### 项目说明

此Python脚本用于自动化识别屏幕上的两个数字，并根据大小关系执行鼠标操作。

在使用 Python 脚本时，**请将模拟器或手机屏幕放到电脑左边半屏。否则会出现问题。**

#### 功能概述

1. **屏幕截图**：截取屏幕指定区域，并保存为图像文件。
2. **OCR识别**：使用Tesseract OCR引擎识别图像中的数字。
3. **比较与操作**：比较两个数字的大小，通过模拟鼠标操作来放大或缩小。

#### 依赖库

- `pytesseract`：用于OCR文本识别。
- `pyautogui`：用于模拟鼠标和键盘操作。
- `cv2`：用于图像处理。
- `numpy`：用于数组操作。
- `os`：用于文件路径操作。
- `time`：用于延时操作。

#### 安装依赖

```bash
pip install pytesseract pyautogui opencv-python numpy
```

#### 运行脚本

1. 确保安装了所有依赖库。

2. 运行脚本：

   ```bash
   python script.py
   ```

#### 文件结构

- `script.py`：主脚本文件。
- `screenLeftOutput.png`：保存左侧截取图像。
- `screenRightOutput.png`：保存右侧截取图像。

#### 主要函数

- `moveMouseBigger()`：模拟鼠标操作以放大。
- `moveMouseSmaller()`：模拟鼠标操作以缩小。
- `getScreen()`：截取屏幕并保存图像。

#### 运行逻辑

1. 持续循环获取屏幕图像。
2. 识别并比较两个数字的大小。
3. 根据结果执行相应的鼠标操作。

#### 注意事项

- 确保屏幕截图区域正确无误。
- 适当调整鼠标操作的位置参数以适应不同屏幕分辨率。

#### 示例输出

```
左边的数字是: 12
右边的数字是: 45
右边的数字大
```

#### 贡献指南

欢迎提交 Issue 或 Pull Request 以改进代码。

#### 许可证

本项目采用MIT许可证。
