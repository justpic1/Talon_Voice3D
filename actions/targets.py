from talon import Module, Context

mod = Module()
ctx = Context()
@mod.capture(rule="<user.letter>")
def base_target(m) -> str:
    "Base targets"
    return m.letter

@mod.action_class
class Actions:
    def voice3d_target(target: str):
        """Move the camera to a specific target"""
        print("something worked here")
        print(target)
        return target