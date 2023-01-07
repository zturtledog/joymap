import time
import pyautogui
import pydirectinput
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

registar = {
    "buttons": {
        "right": {
            "x"  : "",
            "b"  : "",
            "a"  : "",
            "y"  : "",
            "r"  : "",
            "zr" : "",
            "sl" : "",
            "sr" : ""
        },
        "shared": {
            "plus"     : "",
            "l-stick"  : "",
            "capture"  : "",
            "minus"    : "",
            "home"     : "",
            "r-stick"  : ""
        },
        "left": {
            "down"   : "",
            "up"     : "",
            "right"  : "",
            "left"   : "",
            "l"      : "",
            "zl"     : ""
        }
    },
    "analog-sticks": {
        "left": {
            "h-max"     : "",
            "h-min"     : "",
            "h-vector"  : "",
            "v-max"       : "",
            "v-min"       : ""
        },
        "right": {
            "h-max"    : "",
            "h-min"    : "",
            "h-vector" : "",
            "v-max"    : "",
            "v-min"    : ""
        }
    },
    "mouse":{"pos":{"vel": ""}}
}

with open("./mappings.joymap", "r+") as file:
    uprolns = file.read().split("\n")
    lines = []
    for x in uprolns:
        if (len(x.strip()) > 0 and not x.strip().startswith("#")): lines.append({
            "key":x.split("->")[0].strip().split("."),
            "val":x.split("->")[1].strip().split(".")
        })
    for x in lines:
        try:
            registar[x["key"][0]][x["key"][1]][x["key"][2]] = x["val"]
        except:
            print(cl.fg.red+"invalid maping key"+cl.reset)

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
dlkey = False
tmkey = False

# hold
lshct = []

def sorg(v):
    return "h:["+str(round(v["left"]["horizontal"]/1000)-2)+", "+str(round(v["left"]["vertical"]/1000)-2)+"] v:["+str(round(v["right"]["horizontal"]/1000)-2)+", "+str(round(v["right"]["vertical"]/1000)-2)+"]"

def execute(mol):
    if (len(mol)>1):
        if (mol[0] == "key"):
            pydirectinput.press(mol[1])  
        if (mol[0] == "mouse"):
            if (mol[1] == "button-click"): pydirectinput.click()
            if (mol[1] == "button-dbclick"): pydirectinput.doubleClick()
            if (mol[1] == "button-lfclick"): pydirectinput.leftClick()
            if (mol[1] == "button-rtclick"): pydirectinput.rightClick()
            if (mol[1] == "button-mdclick"): pydirectinput.middleClick()
            if (mol[1] == "button-tpclick"): pydirectinput.tripleClick()
        if (mol[0] == "hold"):
            pydirectinput.keyDown(mol[1])
            found = False
            for x in lshct:
                if (x["key"] == mol[1]):
                    x["last-frame"] = True
                    found = True
                    break
            if not found:
                lshct.append({
                    "key":mol[1],
                    "last-frame":True
                })

def mapr(right, left, registar):
    if (right["buttons"]["right"]["x" ]):  execute(registar["buttons"]["right"]["x" ])
    if (right["buttons"]["right"]["b" ]):  execute(registar["buttons"]["right"]["b" ])
    if (right["buttons"]["right"]["a" ]):  execute(registar["buttons"]["right"]["a" ])
    if (right["buttons"]["right"]["y" ]):  execute(registar["buttons"]["right"]["y" ])
    if (right["buttons"]["right"]["r" ]):  execute(registar["buttons"]["right"]["r" ])
    if (right["buttons"]["right"]["zr"]):  execute(registar["buttons"]["right"]["zr"])
    if (right["buttons"]["right"]["sl"]):  execute(registar["buttons"]["right"]["sl"])
    if (right["buttons"]["right"]["sr"]):  execute(registar["buttons"]["right"]["sr"])
    if (right["buttons"]["shared"]["plus"   ]):  execute(registar["buttons"]["shared"]["plus"   ]) 
    if (right["buttons"]["shared"]["l-stick"]):  execute(registar["buttons"]["shared"]["l-stick"]) 
    if (right["buttons"]["shared"]["capture"]):  execute(registar["buttons"]["shared"]["capture"]) 
    if (right["buttons"]["shared"]["minus"  ]):  execute(registar["buttons"]["shared"]["minus"  ]) 
    if (right["buttons"]["shared"]["home"   ]):  execute(registar["buttons"]["shared"]["home"   ]) 
    if (right["buttons"]["shared"]["r-stick"]):  execute(registar["buttons"]["shared"]["r-stick"]) 
    if (left["buttons"]["left"]["down" ]):  execute(registar["buttons"]["left"]["down" ])
    if (left["buttons"]["left"]["up"   ]):  execute(registar["buttons"]["left"]["up"   ])
    if (left["buttons"]["left"]["right"]):  execute(registar["buttons"]["left"]["right"])
    if (left["buttons"]["left"]["left" ]):  execute(registar["buttons"]["left"]["left" ])
    if (left["buttons"]["left"]["l"    ]):  execute(registar["buttons"]["left"]["l"    ])
    if (left["buttons"]["left"]["zl"   ]):  execute(registar["buttons"]["left"]["zl"   ])
    jorrstatus = joyconr.get_status()["analog-sticks"]
    jollstatus = joyconl.get_status()["analog-sticks"]
    if ((round(jollstatus["left"]["horizontal"]/1000)-2) > 1):  execute(registar["analog-sticks"]["left"]["h-max" ])
    if ((round(jollstatus["left"]["horizontal"]/1000)-2) < -1):  execute(registar["analog-sticks"]["left"]["h-min" ])
    if ((round(jollstatus["left"]["vertical"]/1000)-2) > 1):  execute(registar["analog-sticks"]["left"]["v-max" ])
    if ((round(jollstatus["left"]["vertical"]/1000)-2) < -1):  execute(registar["analog-sticks"]["left"]["v-min" ])
    if ((round(jorrstatus["right"]["horizontal"]/1000)-2) > 1):  execute(registar["analog-sticks"]["right"]["h-max" ])
    if ((round(jorrstatus["right"]["horizontal"]/1000)-2) < -1):  execute(registar["analog-sticks"]["right"]["h-min" ])
    if ((round(jorrstatus["right"]["vertical"]/1000)-2)>1):  execute(registar["analog-sticks"]["right"]["v-max" ])
    if ((round(jorrstatus["right"]["vertical"]/1000)-2)>-1):  execute(registar["analog-sticks"]["right"]["v-min" ])
    # -- mouse
    speed = 52
    if (len(registar["mouse"]["pos"]["vel"])>1 and registar["mouse"]["pos"]["vel"][0] != "none"): pyautogui.move(
        (round(jorrstatus[registar["mouse"]["pos"]["vel"][1]]["horizontal"]/1000)-2)*speed,
        (round(jorrstatus[registar["mouse"]["pos"]["vel"][1]]["vertical"]/1000)-2)*-speed)

while True:
    # jorrstatus = joyconr.get_status()["analog-sticks"]
    # pydirectinput.move((round(jorrstatus["right"]["horizontal"]/1000)-2)*speed,(round(jorrstatus["right"]["vertical"]/1000)-2)*-speed,0.1)
    # -- reprint
    def reprint():
        shifting = joyconl.get_status()["buttons"]["left"]["zl"]
        pydirectinput.press("backspace")
        if (shifting): pydirectinput.keyDown('shift')  # hold down the shift key
        pydirectinput.press(charsets[index][subindex])
        if (shifting): pydirectinput.keyUp('shift')    # release the shift key

    # -- typemode stating
    if joyconl.get_status()["buttons"]["left"]["sl"]:
        if (not tmkey):
            typemode = True
            subindex = 0
            index = 0
            #reprint
            shifting = joyconl.get_status()["buttons"]["left"]["zl"]
            if (shifting): pydirectinput.keyDown('shift')  # hold down the shift key
            pydirectinput.press(charsets[index][subindex])
            if (shifting): pydirectinput.keyUp('shift')    # release the shift key
        tmkey = True
    else:
        tmkey = False

    # -- keylog and typemode
    if (joyconr.get_status()["battery"]["level"]<2 and joyconr.get_status()["battery"]["level"]<2):
        print("battery low")
    if (typemode):
        if joyconl.get_status()["buttons"]["left"]["l"]:
            if (not dlkey):
                pydirectinput.press("backspace")
                reprint()
            dlkey = True
        else:
            dlkey = False

        # -- decrement index
        if joyconl.get_status()["buttons"]["left"]["up"]:
            if (not typkey):
                index -= 1
                if (index < 0):
                    subindex = 0
                    index = 0
                reprint()
            typkey = True

        # -- increment index
        elif joyconl.get_status()["buttons"]["left"]["down"]:
            if (not typkey):
                index += 1
                if (index > len(charsets)-1):
                    index = len(charsets)-1
                    subindex = 0
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
    else: 
        mapr(joyconr.get_status(), joyconl.get_status(), registar) 
        fasdy = []
        for x in lshct:
            if not x["last-frame"]:
                pydirectinput.keyUp(x["key"])
            else:
                x["last-frame"] = False
                fasdy.append(x)
    
    
# dbclick
# if (joyconl.get_status()["buttons"]["left"]["up"]):
#     if (not clu):
#         pydirectinput.doubleClick()
#     clu = True
# else:
#     clu = False
# # hold
# if (joyconl.get_status()["buttons"]["left"]["down"]):
#     if (not cld):
#         pydirectinput.click()
#     cld = True
# else:
#     cld = False

# print(clutil.lnup+clutil.lnup+clutil.lnup)
# print(sorg(joyconr.get_status()["analog-sticks"])+"                                                 ")
# print(sorg(joyconl.get_status()["analog-sticks"])+"                                                 ")
# #