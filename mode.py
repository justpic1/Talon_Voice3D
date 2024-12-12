from talon import Module, Context
mod = Module()
ctx = Context()
mod.list("mode_list", desc="modes")
ctx.lists["user.mode_list"] = {
    "faces",
    "joints",
    "edges",
    "objects",
}


@mod.capture(rule="{user.mode_list}")
def modes(m) -> str:
    "Base targets"
    return m.mode_list

@mod.action_class
class Actions:
    def voice3d_mode(action_name: str):
        """Move the camera to a specific target"""
        print("something worked here")
        print(action_name)
        return action_name