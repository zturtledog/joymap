with open("./mappings.joymap", "r+") as file:
    uprolns = file.read().split("\n")
    lines = []
    for x in uprolns:
        if (len(x.strip()) > 0 and not x.strip().startswith("#")): lines.append({
            "key":x.split("->")[0].strip().split("."),
            "val":x.split("->")[1].strip().split(".")
        })
    print(lines)

registar = {
    "buttons": {
        "right": {
            "x"  : "key.e",
            "b"  : "key.shift",
            "a"  : "key.space",
            "y"  : "",
            "r"  : "",
            "zr" : "",
            "sl" : "joy.enable-type-mode",
            "sr" : "joy.disable-type-mode"
        },
        "shared": {
            "plus"     : "key.escape",
            "l-stick"  : "key.ctrl",
            "capture"  : "key.f12",
            "minus"    : "",
            "home"     : "",
            "r-stick"  : ""
        },
        "left": {
            "down"   : "mouse.button-click",
            "up"     : "mouse.button-dbclick",
            "right"  : "key.backspace",
            "left"   : "",
            "l"      : "",
            "zl"     : ""
        }
    },

    "analog-sticks": {
        "left": {
            "horizontal": {
                "max"     : "key.d",
                "min"     : "key.a",
                "vector"  : ""
            },
            "vertical": {
                "max"       : "key.w",
                "min"       : "key.s",
                "vector"    : ""
            }
        },
        "right": {
            "horizontal": {
                "max"    : ".",
                "min"    : ".",
                "vector" : "mouse.velocity-y"
            },
            "vertical": {
                "max"    : "",
                "min"    : "",
                "vector" : "mouse.velocity-x"
            }
        }
    }
}