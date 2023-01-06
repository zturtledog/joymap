import time
import pyautogui
from pyjoycon import JoyCon, get_R_id, get_L_id
import clutil

joycon_idr = get_R_id()
joycon_idl = get_L_id()
joyconr = JoyCon(*joycon_idr)
joyconl = JoyCon(*joycon_idl)

# idcl
clu = False
cld = False

def sorg(v):
    return "h:["+str(round(v["left"]["horizontal"]/1000)-2)+", "+str(round(v["left"]["vertical"]/1000)-2)+"] v:["+str(round(v["right"]["horizontal"]/1000)-2)+", "+str(round(v["right"]["vertical"]/1000)-2)+"]"

while True:
    speed = 32
    jorrstatus = joyconr.get_status()["analog-sticks"]
    pyautogui.move((round(jorrstatus["right"]["horizontal"]/1000)-2)*speed,(round(jorrstatus["right"]["vertical"]/1000)-2)*-speed,0.1)
    # dbclick
    if (joyconl.get_status()["buttons"]["left"]["up"]):
        if (not clu):
            pyautogui.doubleClick()
        clu = True
    else:
        clu = False
    # hold
    if (joyconl.get_status()["buttons"]["left"]["down"]):
        if (not cld):
            pyautogui.click()
        cld = True
    else:
        cld = False

# print(clutil.lnup+clutil.lnup+clutil.lnup)
# print(sorg(joyconr.get_status()["analog-sticks"])+"                                                 ")
# print(sorg(joyconl.get_status()["analog-sticks"])+"                                                 ")
# #