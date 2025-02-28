from talon import Module, actions, Context

from talon import Module, actions, Context

mod = Module()
ctx = Context()
mod.list("prep", desc="describes the direction of a modifier")
ctx.lists["user.prep"] = {
    "to" : "to",
    "from" : "from",
    "away from" : "away from",
    "past" : "past",
    "up" : "up",
    "down" : "down",
    
}