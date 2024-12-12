from talon import Module, Context
mod = Module()
ctx = Context()
mod.list("descriptors")
ctx.lists["user.descriptors"] = {
    "side length" : "side_length",
}
