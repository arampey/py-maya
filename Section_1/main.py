# to run this script from pycharm, paste the following into the maya script editor:
# import maya.cmds as cmds
# if not cmds.commandPort(':4434', q=True):
#   cmds.commandPort(n=':4434')

from maya import cmds

# the first position is the object itself, the second position is the name of the maya node that created the cube
cube = cmds.polyCube()
cubeShape = cube[0]

circle = cmds.circle()
circleShape = circle[0]

# the first entry is the child, the second should be the parent
cmds.parent(cubeShape, circleShape)

# lock attributes; tx locks only the x transform
cmds.setAttr(cubeShape + ".translate", lock=True)
cmds.setAttr(cubeShape + ".rotate", lock=True)
cmds.setAttr(cubeShape + ".scale", lock=True)

# select the circle since the cube is locked
cmds.select(circleShape)