from Detect_Color_04 import Create_Color
from Detect_Color_04 import Detect_Color

def Invoke_Create_Colors_Func(frame):
    return [
        lambda: Create_Color(frame, [170, 130, 100], [180, 255, 255], 800, "Red", (0, 0, 255)),
        lambda: Create_Color(frame, [110, 180, 0], [116, 255, 255], 800, "Blue", (255, 0, 0)),
        lambda: Create_Color(frame, [40, 150, 20], [70, 255, 255], 800, "Green", (0, 255, 0)),
        lambda: Create_Color(frame, [2.5, 140, 100], [13, 255, 255], 800, "Orange", (6, 100, 255)),
        lambda: Create_Color(frame, [17.5, 100, 100], [30, 255, 255], 800, "Yellow", (6, 255, 255)),
        lambda: Create_Color(frame, [95, 112, 120], [108, 255, 255], 800, "Cyan", (255, 255, 0)),
        lambda: Create_Color(frame, [118, 100, 100], [130, 255, 255], 800, "Purple", (128, 0, 128)),
        lambda: Create_Color(frame, [0, 0.2, 0.2], [0, 32, 32], 800, "Black", (0, 2, 2)),
        lambda: Create_Color(frame, [135, 100, 100], [160, 255, 255], 800, "Pink", (255, 0, 255)),
        lambda: Create_Color(frame, [0, 0, 0], [80, 80, 80], 800, "Gray", (128, 128, 128))
        # Add colors here (same format) (frame, hsv_range_lower, hsv_range_upper, min_area, name, BGR)
    ]

cam0 = Detect_Color()
cam0.Assign_Camera(0) # 0 is default camera id, increase it gradually for selecting your desired camera
cam0.Start_Detection(Invoke_Create_Colors_Func)
