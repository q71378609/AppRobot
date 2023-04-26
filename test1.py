from myclass.device import device

global_config = {
    'emulator-5554':{
    
    }
}
a = device('emulator-5554',global_config['emulator-5554'])
a.reset()