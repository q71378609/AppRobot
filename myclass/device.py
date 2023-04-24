import subprocess

class device:
    def __init__(self,s) -> None:
        out, err = subprocess.Popen('adb.exe devices',shell=True,stdout=subprocess.PIPE).communicate()
        out, err = subprocess.Popen('adb.exe devices',shell=True,stdout=subprocess.PIPE).communicate()
        out = out.decode('utf-8').split('\r\n')[1:-2]
        for i in out:
            if s == i.split('\t')[0]:
                self.name = s
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

    def reset(self):
        result = subprocess.Popen('adb.exe -s '+self.name+' shell input keyevent 187',shell=True,stdout=subprocess.PIPE)
        out, err = result.communicate()
