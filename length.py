from talon import Module, Context

mod = Module()
ctx = Context()

@mod.capture(rule="<user.number_prose_with_dot> [{user.unit}]")
def length(m) -> str:
    print("length")
    return m