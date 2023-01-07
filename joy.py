import time
import pyautogui
from pyjoycon import JoyCon, get_R_id, get_L_id
import clutil as cl

try:
    joycon_idr = get_R_id()
    joycon_idl = get_L_id()
    joyconr = JoyCon(*joycon_idr)
    joyconl = JoyCon(*joycon_idl)
except BaseException:
   print (cl.fg.red+"probably a conection error"+cl.reset+"\n  make sure that the joycons are on and paired\n  ensure that the joycons are paired in the correct order")
   exit()

print("battery: "+str(joyconr.get_status()["battery"]["level"])+"/4 and "+str(joyconr.get_status()["battery"]["level"])+"/4")

charsets = [
    "qwertyuiopasdfghjklzxcvbnm",
    "1234567890",
    "}{[]()\"'!&|/#,.?:=+-*%;^_\\<>~`@$",
    " \n\t"
]
typemode = False
subindex = 0
index = 0

# idcl
typkey = False
tpbck = False
clu = False
cld = False

def sorg(v):
    return "h:["+str(round(v["left"]["horizontal"]/1000)-2)+", "+str(round(v["left"]["vertical"]/1000)-2)+"] v:["+str(round(v["right"]["horizontal"]/1000)-2)+", "+str(round(v["right"]["vertical"]/1000)-2)+"]"

while True:
    speed = 32
    jorrstatus = joyconr.get_status()["analog-sticks"]
    pyautogui.move((round(jorrstatus["right"]["horizontal"]/1000)-2)*speed,(round(jorrstatus["right"]["vertical"]/1000)-2)*-speed,0.1)
    # -- reprint
    def reprint():
        shifting = joyconl.get_status()["buttons"]["left"]["zl"]
        pyautogui.press("backspace")
        if (shifting): pyautogui.keyDown('shift')  # hold down the shift key
        pyautogui.press(charsets[index][subindex])
        if (shifting): pyautogui.keyUp('shift')    # release the shift key

    # -- typemode stating
    if joyconl.get_status()["buttons"]["left"]["sl"]:
        typemode = True
        subindex = 0
        index = 0
        #reprint
        shifting = joyconl.get_status()["buttons"]["left"]["zl"]
        if (shifting): pyautogui.keyDown('shift')  # hold down the shift key
        pyautogui.press(charsets[index][subindex])
        if (shifting): pyautogui.keyUp('shift')    # release the shift key

    # -- keylog and typemode
    if (joyconr.get_status()["battery"]["level"]<2 and joyconr.get_status()["battery"]["level"]<2):
        print("battery low")
    if (typemode):
        if joyconl.get_status()["buttons"]["left"]["l"]:
            pyautogui.press("backspace")
            reprint()

        # -- decrement index
        if joyconl.get_status()["buttons"]["left"]["up"]:
            if (not typkey):
                index -= 1
                if (index < 0):
                    index = 0
                reprint()
            typkey = True

        # -- increment index
        elif joyconl.get_status()["buttons"]["left"]["down"]:
            if (not typkey):
                index += 1
                if (index > len(charsets)-1):
                    index = len(charsets)-1
                reprint()
            typkey = True

        # -- decrement charid
        elif joyconl.get_status()["buttons"]["left"]["left"]:
            if (not typkey):
                subindex -= 1
                if (subindex < 0):
                    subindex = 0
                reprint()
            typkey = True

        # -- increment charid
        elif joyconl.get_status()["buttons"]["left"]["right"]:
            if (not typkey):
                subindex += 1
                if (subindex > len(charsets[index])-1):
                    subindex = len(charsets[index])-1
                reprint()
            typkey = True

        # -- unkey
        else: typkey = False

        # -- exit typemode
        if joyconl.get_status()["buttons"]["left"]["sr"]:
            typemode = False
    #else:
    #    print(0)
    
    
    
# dbclick
# if (joyconl.get_status()["buttons"]["left"]["up"]):
#     if (not clu):
#         pyautogui.doubleClick()
#     clu = True
# else:
#     clu = False
# # hold
# if (joyconl.get_status()["buttons"]["left"]["down"]):
#     if (not cld):
#         pyautogui.click()
#     cld = True
# else:
#     cld = False

# print(clutil.lnup+clutil.lnup+clutil.lnup)
# print(sorg(joyconr.get_status()["analog-sticks"])+"                                                 ")
# print(sorg(joyconl.get_status()["analog-sticks"])+"                                                 ")
# #