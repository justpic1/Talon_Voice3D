from talon import Module, actions, Context
import numpy as np
mod = Module()
ctx = Context()
mod.list("anatomical_positions", desc="Anatomical positions")
ctx.lists["user.anatomical_positions"] = {
    "right": "dexter",
    "left": "sinister",
    "dext": "dexter",
    "sin": "sinister",
    "front": "anterior",
    "back": "posterior",
    "ant": "anterior",
    "post": "posterior",
    "top": "superior",
    "bottom": "inferior",
    "soup": "superior",
    "inf": "inferior",
}


@mod.capture(rule="{user.anatomical_positions}")
def anatomical_positions(m) -> str:
    "Anatomical positions"
    pos_to_vec = {
        "dexter": [1, 0, 0],
        "sinister": [-1, 0, 0],
        "superior": [0, 0, 1],
        "inferior": [0, 0, -1],
        "anterior": [0, -1, 0],
        "posterior": [0, 1, 0],
    }
    vec3 = pos_to_vec[m.anatomical_positions]
    return " ".join([str(i) for i in vec3])
@mod.action_class
class Actions:
    def voice3d_view(position: list[str]):
        """Move the camera to a specific position"""
        print("something worked here")
        position = np.sum([np.array(i.split()).astype(int) for i in position], axis=0)
        actions.user.send_rpc_message(
            f"command: camera_move\n"
            "\n"
            f"destination:  |   | {position[0]} {position[1]} {position[2]}"
        )
    def voice3d_view_target(target: str):
        """Move the camera to view a specific target"""
        print("something worked here")
        print(target)