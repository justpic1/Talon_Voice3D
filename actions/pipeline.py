# file may never be used, pipeline is a concept for now

from talon import Module, Context
mod = Module()
ctx = Context()

@mod.capture(rule= 
            "{user.objects_2d_list} | "
            "{user.objects_3d_list} | "
            "{user.descriptors} | "
            "{user.targets} | "
            "{user.actions}"
            )
def pipeline(m) -> str:
    "Base targets"
    return m


@mod.capture(rule="<user.pipeline>+")
def commands(pipeline:str) -> str:
    # abbreviate the pipeline and parses it
    "Base targets"
    return pipeline