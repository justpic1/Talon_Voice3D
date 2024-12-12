from talon import Module, Context

mod = Module()
ctx = Context()

mod.list("objects_3d_list", desc="List of 3D objects")
ctx.lists["user.objects_3d_list"] = {
    "cube": "cube",
    "sphere": "sphere",
    "cone": "cone",
    "cylinder": "cylinder",
    "pyramid": "pyramid",
    "prism": "prism",
    "torus": "torus",
    "hedron": "hedron",
}

@mod.capture(rule="{user.objects_3d_list}")
def objects_3d(m) -> str:
    "Base targets"
    return m.objects_3d_list

@mod.action_class
class Actions:
    def voice3d_create(action_name: str):
        """Create a specific object"""
        print("something worked here")
        print(action_name)
        return action_name