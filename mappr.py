# "buttons":{
#     "right":{
#         x  -> key.e
#         b  -> key.shift
#         a  -> key.space
#         y  -> .
#         r  -> .
#         zr -> .
#         sl -> joy.enable-type-mode
#         sr -> joy.disable-type-mode
#     }
#     "shared":{
#         plus     -> key.escape
#         l-stick  -> key.ctrl
#         capture  -> key.f12
#         minus    -> .
#         home     -> .
#         r-stick  -> .
#     }
#     left.down   -> mouse.button-click
#     left.up     -> mouse.button-dbclick
#     left.right  -> key.backspace
#     left.left   -> .
#     left.l      -> .
#     left.zl     -> .
# }

# analog-sticks.left.h-max     -> key.d
# analog-sticks.left.h-min     -> key.a
# analog-sticks.left.h-vector -> .
# analog-sticks.left.v-max       -> key.w
# analog-sticks.left.v-min       -> key.s
# analog-sticks.left.v-vector   -> .
# analog-sticks.right.h-max  -> .
# analog-sticks.right.h-min  -> .
# analog-sticks.right.h-vector -> mouse.velocity-y
# analog-sticks.right.v-max    -> .
# analog-sticks.right.v-min    -> .
# analog-sticks.right.v-vector   -> mouse.velocity-x




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
    if (left["analog-sticks"]["left"]["h-max" ] ):  execute(registar["analog-sticks"]["left"]["h-max" ] )
    if (left["analog-sticks"]["left"]["h-min" ] ):  execute(registar["analog-sticks"]["left"]["h-min" ] )
    if (left["analog-sticks"]["left"]["v-max" ] ):  execute(registar["analog-sticks"]["left"]["v-max" ] )
    if (left["analog-sticks"]["left"]["v-min" ] ):  execute(registar["analog-sticks"]["left"]["v-min" ] )
    if (left["analog-sticks"]["left"]["vector"] ):  execute(registar["analog-sticks"]["left"]["vector"] )
    if (right["analog-sticks"]["right"]["h-max" ]):  execute(registar["analog-sticks"]["right"]["h-max" ])
    if (right["analog-sticks"]["right"]["h-min" ]):  execute(registar["analog-sticks"]["right"]["h-min" ])
    if (right["analog-sticks"]["right"]["v-max" ]):  execute(registar["analog-sticks"]["right"]["v-max" ])
    if (right["analog-sticks"]["right"]["v-min" ]):  execute(registar["analog-sticks"]["right"]["v-min" ])
    if (right["analog-sticks"]["right"]["vector"]):  execute(registar["analog-sticks"]["right"]["vector"])

def execute(mol):
    print(mol)