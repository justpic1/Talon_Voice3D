from talon import Module, actions, Context
mod = Module()
mod.list("voice3d_action_list", desc="List of voice3d actions")
ctx = Context()
@mod.action_class
class Actions:
    def add(a: int, b: int) -> int:
        """Adds two numbers"""
        return a + b