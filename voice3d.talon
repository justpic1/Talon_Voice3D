#commands such as gui file would press the file button in the gui
gui <user.gui_command>:
    user.voice3d_command(gui_command)

# commands such as view ant soup would use anatomical positions to describe 
# which orientation to view the object
view <user.anatomical_positions>+:
    user.voice3d_view(anatomical_positions_list)

# commands such as view air would find the token object air and view it head on
view <user.base_target>:
    user.voice3d_view(base_target)

# commands such as focus air would find the token object air and focus on it
# giving it the root of the camera rotation
focus <user.base_target>:
    user.voice3d_focus(base_target)

# commands such as "draw square" and "draw square on air" would draw a square
draw <user.objects_2d> [<prep> <location>]:
    user.voice3d_draw(objects_2d)

# commands such as "create cube" and "create cube on air" would create a cube
create <user.objects_3d>:
    user.voice3d_create(objects_3d)

# commands such as "move air" and "move air to bat" would move the object air
move <user.object>:
    user.voice3d_move(move_target)


modify <user.target>:
    user.voice3d_modify(modify_target)

# commands such as "delete air" and "delete air and bat" 
# would delete the object air or air and bat
delete <user.target>:
    user.voice3d_delete(delete_target)

# commands such as "faces" would give the faces target decorators
<user.modes>:
    user.voice3d_mode(modes)



#<user.commands>:
#    print("hi")
