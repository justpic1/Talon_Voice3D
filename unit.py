from talon import Module, actions, Context

mod = Module()
ctx = Context()
mod.list("unit", desc="unit of measurement")
ctx.lists["user.unit"] = {
    "millimeters": "mm",
    "centimeters": "cm",
    "meters": "m",
    "inches": "in",
    "feet": "ft",
    "yards": "yd",
}




