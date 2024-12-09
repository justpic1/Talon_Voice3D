from talon import Context, actions, Module
mod = Module()
ctx = Context()
#ctx.tags = ["user.voice3d"]
mod.list("gui_action_list", desc="List of GUI actions")
ctx.lists["user.gui_action_list"] = {
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


@mod.capture(rule="{user.gui_action_list}")
def gui_command(m) -> dict[str, str]:
    "Capture a gui command"
    value = m.gui_action_list
    print(value)
    print("at least this worked")
    return {
        "value": value,
        "type": "gui_action",
    }

@mod.action_class
class Actions:
    def voice3d_command(action_name: dict):
        """Perform voice3d command"""
        print("something worked here")
        actions.user.add(1, 2)