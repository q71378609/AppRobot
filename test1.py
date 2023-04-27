from myclass.device import device

global_config = {
    'emulator-5554':{
        'qmmfxs':{
            
        },
        'wkllq':{
    
        }
    }
}
a = device('emulator-5554',global_config['emulator-5554'])
a.apptasks[0].start()
#a.reset()