from talon import Context, actions, Module

gui_actions = {
    "close": "close",
    "copy": "copy",
    "cut": "cut",
    "delete": "delete",
    "find": "find",
    "go back": "goBack",
    "go forward": "goForward",
    "go to line": "gotoLine",
    "indent": "indent",
    "open": "open",
    "paste": "paste",
    "redo": "redo",
    "save": "save",
    "save all": "saveAll",
    "select all": "selectAll",
    "undo": "undo",
}

draw_actions = {
    "draw line": "drawLine",
    "draw circle": "drawCircle",
    "draw rectangle": "drawRect",
    "draw square": "drawSquare",
    "draw text": "drawText",
}

create_actions = {
    "create cube": "createCube",
    "create sphere": "createSphere",
    "create cylinder": "createCylinder",
    "create cone": "createCone",
    "create plane": "createPlane",
}
modify_actions = {
}
delete_actions = {
}
camera_actions = {
    "camera move": "cameraMove",
    "camera rotate": "cameraRotate",
    "camera zoom": "cameraZoom",
}