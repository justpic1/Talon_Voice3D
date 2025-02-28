from talon import Module, actions, Context
mod = Module()
ctx = Context()
mod.list("color", desc="Colors")
ctx.lists["user.color"] = {
    "red": "red",
    "green": "green",
    "blue": "blue",
    "yellow": "yellow",
    "orange": "orange",
    "purple": "purple",
    "pink": "pink",
    "brown": "brown",
    "black": "black",
    "white": "white",
    "gray": "gray",
    "cyan": "cyan",
    "magenta": "magenta"
}