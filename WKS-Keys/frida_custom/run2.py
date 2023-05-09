import frida
import time
import sys 

lic = ""
def on_message(message, data):
    global lic
    lic = message['payload']

def getLic():
    return lic
# load script from file
def parse_hook(filename):
    print('[*] Parsing hook: ' + filename)
    hook = open(filename, 'r')
    script = session.create_script(hook.read())
    script.on('message', on_message)
    script.load()
    return script

def loadScript(script):
    script = session.create_script(script)
    script.on('message', on_message)
    script.load()
    return script

# get device
device = frida.get_usb_device()
print("[+] Current device:")
print(device)

# spawning wanted app
app = "com.fplay.activity"
# get pid
pid = None
for a in device.enumerate_applications():
    if a.identifier == app:
        pid = a.pid
        break
# attach app to session
session = device.attach(pid)

# hook our script
# testLicense = 'U01XVgAABAMAAACLAnwEDw0IEIINuNJG6Vm3EjGm0YbYVOgAAABsyvI6Rcj6ZuniKsNqPgoj9IChF34sIQ3RFw3GvTCi0uEbDP9jV1eAzS0m3UH9QrSzbDEXCyi9QFFkuDU2wRYp99G+4bB8cRMs/nbxAesPAD+W/8bQSiSlU6GIkWNuKWVnKGhhJaRZZcipDxRoe0wbFsisyiTpXZpNz46C23M0aD5WuAbBENP92CtoF93IL9dv8CoTyqrrhu3n1nnTxc211wq21KC53E94D2XX71LSAyjEB8djYIV+G8Jj+JvchrETqCJ+2RfKFUTKn6aMHMpjnV8ai1a4QyFEAPIT64WRYs0h5myZrmY27gkX917OxTXNV830KdjLUsESV56CMlB2TKZtwYQG6K9omYNJtfHy++CnDpxKARSC3R5YB7Wjic+mxhZRl0jo0LZVG7szzIza7LHc4V6zF10y+YBAkG2qVGF9ZdvjV7h+YIV8JEH5jhIKmVhtgAo7j8tKdyPU1vMc7sbg8MmF8N0tF07hlKQ/4o4m6he6I4Dz5wmSyBWmJY9EemnqXSX1sAhhivzZe3bsD2xX4bSr5X7hO6q4nAumH/eGGqByGW+WoK1vzeEDu6fJx3xt1vS+9ZlXEfs3U2uavAb4nOTyB8FcWhNSpm5lvyp/QCP2aA7uyCpd9ihT4B3HYQ284AQwxSzV0RFuX95ZHyFWt6NBvTus4UcffHRmt3Ta+1AUrbadvZJMD3kMFWtciwKdcNRk6xiRIzXJPMW3OY3+zmmm4uY1kMNEICPh/wVxiNVxaAHIKaQL5y+IUpu7tqI2G23G1/MxnkPOpNwmGaPrS4Xg1xlBeukPloi0cvVZwr8nzYD/6fEsscjJDBJmUK3wkP/m3UZtfx1gC2s55I4A03H0ffAio+G5+ij6PJa/ePD0vYBW30haIBPCg/xiB1wpgkOwlhAsyjSqY6ql50jLzgrEqnRqwIUvrdnPXCBGVqh1T0uytJGD+SJOek1igT6GlFRaRtLsKJNG8/dCF3IRmYVdLJkv52FMwPTJnmq+M6k9hV8nFtCzi1J6XcElQzPUBzEwZwam+4ivv9yIZtbi38iPPqUZ7Btv9YcmjjRNRcd8Zh7tQPZI7wChgFJKQAlGG8jhp/qqLoghatPVi3cHkN+NqcTxLPtD2NU7hyIqPwEGWq6j0v+2CwfZnGd2F8C8xwPao4wfnz8b41T8yvuah40F0PMnpv/0uueSc5ZsS40LbRUIzXY+KTAj3AVD2AVsmSDKxL22mBu6MCdUxk1NM+0qRwb3SDM0ph/4ADApQkxWz49MzZnx0UNijhNpqg/n0jXWsqYT2Qps5kTbsQ4PWCw2c5hn2Qe5Tw=='
def extract_license(testLicense):
    filename = "./frida_custom/extractLicense.js"
    hook = open(filename, 'r').read()
    hook = hook + "extractLicense(\"" + testLicense + "\")"
    # script = parse_hook(hook_script)
    loadScript(hook)
    return getLic()

# sys.stdin.read() # MUST HAVE THIS TO PREVENT THE SCRIPT FINISH