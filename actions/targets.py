from talon import Module, Context

mod = Module()
ctx = Context()
mod.list("base_target_list", desc="Base targets")
ctx.lists["user.base_target_list"] = {
    "air" : "a",
    "bat" : "b"
}
@mod.capture(rule="{user.base_target_list}")
def base_target(m) -> str:
    "Base targets"
    return m.base_target_list

@mod.action_class
class Actions:
    def voice3d_target(target: str):
        """Move the camera to a specific target"""
        print("something worked here")
        print(target)
        return target