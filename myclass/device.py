import subprocess

class device:
    def __init__(self,s) -> None:
        out, err = subprocess.Popen('adb.exe devices',shell=True,stdout=subprocess.PIPE).communicate()
        out, err = subprocess.Popen('adb.exe devices',shell=True,stdout=subprocess.PIPE).communicate()
        print('开始枚举设备...')
        print(out)
        pass

    def ADB(self,cmd,s):
        result = subprocess.Popen('adb.exe -s '+s+' '+cmd,shell=True,stdout=subprocess.PIPE)
        out, err = result.communicate()
        # return out.replace(b'\r\r\n', b'\n') #Android6及以下
        return out.replace(b'\r\n', b'\n') #Android7及以上