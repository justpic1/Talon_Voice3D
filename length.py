from talon import Module, Context

mod = Module()
ctx = Context()

@mod.capture(rule="<user.number_string> [{user.unit}]")
def length(m) -> str:
    print("length")
    return m