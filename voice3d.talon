gui <user.gui_command>:
    user.voice3d_command(gui_command)

view <user.anatomical_positions>+:
    user.voice3d_view(anatomical_positions_list)

face <user.base_target>:
    print("face " + base_target)

draw <user.2D_object>:
    user.voice3d_draw(draw_target)

create <user.3D_object>:
    user.voice3d_create(create_target)

move <user.object>:
    user.voice3d_move(move_target)

modify <user.target>:
    user.voice3d_modify(modify_target)

delete <user.target>:
    user.voice3d_delete(delete_target)
