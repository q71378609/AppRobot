import subprocess
import cv2
import numpy as np
class device:
    def __init__(self,s,config) -> None:
        out, err = subprocess.Popen('adb.exe devices',shell=True,stdout=subprocess.PIPE).communicate()
        out, err = subprocess.Popen('adb.exe devices',shell=True,stdout=subprocess.PIPE).communicate()
        out = out.decode('utf-8').split('\r\n')[1:-2]
        for i in out:
            if s == i.split('\t')[0]:
                self.name = s
                self.config = config
                print('设备:\t'+s+'\t生成...')
                self.get_wm_size()
                print('设备分辨率:\tx_{}\ty_{}'.format(self.wm_x,self.wm_y))
                return
            #devices.append(i.split('\t')[0])
        raise Exception("指定设备不存在...")

    def ADB(self,cmd,s):
        result = subprocess.Popen('adb.exe -s '+s+' '+cmd,shell=True,stdout=subprocess.PIPE)
        out, err = result.communicate()
        # return out.replace(b'\r\r\n', b'\n') #Android6及以下
        return out.replace(b'\r\n', b'\n') #Android7及以上
    
    def get_wm_size(self):
        re = self.ADB('shell wm size',self.name)[15:].decode('utf-8').split('x',1)
        self.wm_x,self.wm_y = int(re[0]),int(re[1])

    def get_sc(self):
        self.screenshot = cv2.imdecode(np.frombuffer(self.ADB('shell screencap -p',self.name), np.uint8), cv2.IMREAD_COLOR)

    def get_xy_img(self,img):
        _img = cv2.imread(img, cv2.IMREAD_COLOR)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(cv2.matchTemplate(self.screenshot, _img, cv2.TM_CCORR_NORMED))
        return max_val,max_loc
    
    def flash_and_find_img(self,img):
        self.get_sc()
        return self.get_xy_img(img)

    def reset(self):
        result = subprocess.Popen('adb.exe -s '+self.name+' shell input keyevent 187',shell=True,stdout=subprocess.PIPE)
        out, err = result.communicate()
        _,xy = self.flash_and_find_img('icon\\device\\reset.png')
        self.ADB('shell input tap {} {}'.format(xy[0],xy[1]),self.name)

