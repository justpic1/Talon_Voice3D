# todo: actions that modify a target: Extrude, Rotate, Scale, etc.
from talon import Module, actions, Context
import numpy as np
mod = Module()
ctx = Context()
mod.list("modifier", desc="Modifiers")
ctx.lists["user.modifier"] = {
    "extrude": "extrude",
    "push pull": "push_pull",
    "fillet": "fillet",
    "chamfer": "chamfer",
    "rotate": "rotate",
    "scale": "scale",
    "mirror": "mirror",
    "move": "move",
    "copy": "copy",
    "array": "array",
    "move": "move",
    "offset" : "offset",
    "undo" : "undo",
    "redo" : "redo",
}

@mod.action_class
class Actions:
    def voice3d_modify(modifier: str, targets: str, length: str, prep: str, destination: str):
        """Apply a modifier to the current selection"""
        print("something worked here")
        print(
            f"command: {modifier}\n"
            f"targets: {targets}\n"
            f"destination: {length} | {prep} | {destination}"
            )
        actions.user.send_rpc_message(
            f"command: {modifier}\n"
            f"targets: {targets}\n"
            f"destination: {length} | {prep} | {destination}"
        )
        return modifier
    
