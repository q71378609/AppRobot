class apptask:
    def __init__(self,name,device) -> None:
        _,self.xy =device.flash_and_find_img('icon\\app\\'+name+'.png')
        self.name = name
        self.device = device

    def start(self):
        self.device.tap(self.xy)