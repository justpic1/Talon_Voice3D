from talon import Module, Context
mod = Module()
ctx = Context()
mod.list("objects_2d_list", desc="List of 2D objects")
ctx.lists["user.objects_2d_list"] = {
    "circle": "circle",
    "square": "square",
    "triangle": "triangle",
    "star": "star",
    "para": "parallelogram",
    "trap": "trapezoid",
    "rect": "rectangle",
}


@mod.capture(rule="{user.objects_2d_list}")
def objects_2d(m) -> str:
    "Base targets"
    return m.objects_2d_list

@mod.action_class
class Actions:
    def voice3d_draw(action_name: str):
        """Move the camera to a specific target"""
        print("something worked here")
        print(action_name)
        return action_name