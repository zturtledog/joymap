with open("./mappings.joymap", "r+") as file:
    uprolns = file.read().split("\n")
    lines = []
    for x in uprolns:
        if (len(x.strip()) > 0 and not x.strip().startswith("#")): lines.append({
            "key":x.split("->")[0].strip().split("."),
            "val":x.split("->")[1].strip().split(".")
        })
    for x in lines:
        registar[x["key"][0]][x["key"][1]][x["key"][2]] = x["val"]

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
            "v-min"       : "",
            "v-vector"    : ""
        },
        "right": {
            "h-max"    : "",
            "h-min"    : "",
            "h-vector" : "",
            "v-max"    : "",
            "v-min"    : "",
            "v-vector" : ""
        }
    }
}
