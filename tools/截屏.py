import subprocess
import time
import numpy as np
import cv2
import os
 
def ADB(cmd):
    result = subprocess.Popen('adb.exe '+cmd,shell=True,stdout=subprocess.PIPE)
    out, err = result.communicate()
    # return out.replace(b'\r\r\n', b'\n') #Android6及以下
    return out.replace(b'\r\n', b'\n') #Android7及以上
def CAP():
    No_Error = True
    try:
        img = ADB('shell screencap -p')
        sc = cv2.imdecode(np.frombuffer(img, np.uint8), cv2.IMREAD_COLOR)
    except:
        print("无法获取屏幕信息！")
        No_Error = False
    if No_Error:
        global screenshot
        screenshot = sc
        cv2.imwrite('sc.png',screenshot)
        #cv2.imshow("UmaShell", screenshot)
        cv2.waitKey(5)


CAP()
#os.system("pause")