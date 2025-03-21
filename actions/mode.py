from talon import Module, Context, actions
mod = Module()
ctx = Context()
mod.list("mode_list", desc="modes")
ctx.lists["user.mode_list"] = {
    "faces",
    "vertices",
    "edges",
    "objects",
    "all",
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
        modifier = action_name
        targets = action_name
        length = ""
        prep = ""
        destination = ""

        actions.user.send_rpc_message(
            f"command: {modifier}\n"
            f"targets: {targets}\n"
            f"destination: {length} | {prep} | {destination}"
        )
        return action_name