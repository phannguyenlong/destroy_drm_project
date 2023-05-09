# -*- coding: utf-8 -*-
# Module: KEYS-L3
# Created on: 11-10-2021
# Authors: -∞WKS∞-
# Version: 1.1.0

import base64, requests, sys, xmltodict
import headers
from pywidevine.L3.cdm import cdm, deviceconfig
from base64 import b64encode
from pywidevine.L3.getPSSH import get_pssh
from pywidevine.L3.decrypt.wvdecryptcustom import WvDecrypt
from frida_custom import run2
import time

pssh = input('\nPSSH: ')
lic_url = input('License URL: ')

def WV_Function(pssh, lic_url, cert_b64=None):
    wvdecrypt = WvDecrypt(init_data_b64=pssh, cert_data_b64=cert_b64, device=deviceconfig.device_android_generic)                   
    widevine_license = requests.post(url=lic_url, data=wvdecrypt.get_challenge(), headers=headers.headers, verify=False)
    license_b64 = b64encode(widevine_license.content)
    
    print("We got: ")
    print(license_b64)
    
    wvdecrypt.update_license(license_b64)

    Correct, keyswvdecrypt = wvdecrypt.start_process()
    if Correct:
        return Correct, keyswvdecrypt   

def WV_Function2(pssh, lic_url,cert_b64=None):
    wvdecrypt = WvDecrypt(init_data_b64=pssh, cert_data_b64=cert_b64, device=deviceconfig.device_android_generic)                   
    widevine_license = requests.post(url=lic_url, data=wvdecrypt.get_challenge(), headers=headers.headers, verify=False)
    widevine_license = widevine_license.json()["license"]
    # license_b64 = b64encode(widevine_license.content)
    license_b64 = widevine_license
    license_b64 = run2.extract_license(license_b64)
    license_b64 = run2.getLic()
    print("========================================")
    print(license_b64)

    wvdecrypt.update_license(license_b64)
    Correct, keyswvdecrypt = wvdecrypt.start_process()
    if Correct:
        return Correct, keyswvdecrypt   

# license_b64 = "CAIS0wIKVAogQTdFQzJFQzg4Mjg3MzVGMTM1MDAwMDAwMDAwMDAwMDASIEE3RUMyRUM4ODI4NzM1RjEzNTAwMDAwMDAwMDAwMDAwGgAgASgAOABAAEjr5eKiBhICCAEaZhIQQ8sE5vzoiY7tcyAjjKVxGxpQ6qWCbIsk1JW9LJAwlKdRa3negXycIsbs7XW/6wcH8XmamnY6GwZfUc/AzORTFhOV0XHb0DxUZYFjqtQi9TWRLrK/sI0isf/GTXpPyWONp5ggARqCAQoQkBSRcI0BQuOqtLV50P7xvhIQuqMeGf0iH3aWFaNk13KVxhogOjsmmFyLHhnSjHAqWaPpQpnBORqdXpjVWQ5fBtWi0oYgAigBQjQKIDYwAykv30LJgTYsH+flufbwLJ08t4kMsJbmSQy+TrEPEhA1QXFTHBgzkaSGXS07+DIoYgAg6+XiogY449yVmwYaICMTzEohslbC+sl/Hu4OjAY6n6b04KlvntFOjxSYBz0mIoACfGgnfDadClUkmbK1WGBGPVqQi1ACgScudrLy7FwFeQ7Wpv+i1Af0yHBNbE1Po2VsLlgPNeGtvIUQFPHVZCei/ue/D4LfgDM9Yt73+3DJWpAccBswRUg+teXuULtoZPaVW0sTNYFrgg3CJmMcxUsRr31HRmp2BcnYVJJYGTePsFCh2GJIU9B5zslMf833bsF9HIbr3J0D9f/q93mDJF88NgEU54BgK1X66nnHcYnUZG1VePAlTX7hziIM2SX/+rXNeIRBdvik9xs7bZdz5zjq0fN7lEhra0iWnI+WmHtSPR88LX7nhiNXDHdzRjfOC0WZ1GzntzjHPBBsJN1Jig7WNzozCjExOC4wLjEgQnVpbHQgb24gQXByIDI0IDIwMjMgMTQ6MzU6MzQgKDE2ODIzNzIwNjkpQAFKsAEAAAACAAAAsAAEABCn2TG7AAAAAAAAAF4AAAAQAAAAcAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAMcAAAAQAAAA2QAAABAAAADrAAAAEAAAATUAAAAQAAABEwAAACAumbgG5lW1L7LY8L26ZN/m5abIvk4B11WQ3Rr8IWz5XlgA"
correct, keys = WV_Function2(pssh, lic_url)

print()
for key in keys:
    print('--key ' + key)
