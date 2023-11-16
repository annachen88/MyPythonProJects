"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

The Brick Game
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 15        # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    total_bricks = graphics.b_r * graphics.b_c

    # Add the animation loop here!
    global NUM_LIVES
    while NUM_LIVES > 0 and total_bricks > 0:
        pause(FRAME_RATE)
        dx = graphics.get_ball_x()
        dy = graphics.get_ball_y()
        graphics.ball.move(dx, dy)
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.set_ball_dx(-dx)
        if graphics.ball.y <= 0 or graphics.ball.y + graphics.ball.height >= graphics.window.height:
            graphics.set_ball_dy(-dy)

        # get object
        maybe_obj_tl = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)

        if maybe_obj_tl:
            # check get object --> paddle
            is_ball_x_in_paddle = (graphics.paddle.x < graphics.ball.x < graphics.paddle.x + graphics.paddle.width) or (graphics.paddle.x < graphics.ball.x + graphics.ball_radius*2 < graphics.paddle.x + graphics.paddle.width)
            is_ball_y_in_paddle = (graphics.paddle.y < graphics.ball.y < graphics.paddle.y + graphics.paddle.height) or (graphics.paddle.y < graphics.ball.y + graphics.ball_radius*2  < graphics.paddle.y + graphics.paddle.height)
            if is_ball_x_in_paddle and is_ball_y_in_paddle:
                # object is paddle
                graphics.ball_xy()
                graphics.set_ball_dx(-dx)
                graphics.set_ball_dy(-dy)
            else:
                # object is bricks
                graphics.ball_xy()
                graphics.window.remove(maybe_obj_tl)
                total_bricks -= 1

        # over the bottom
        if graphics.ball.y + graphics.ball_radius*2 >= graphics.window.height or graphics.ball.y == graphics.window.height:
            # minus the life time
            NUM_LIVES -= 1
            graphics.ball.x = (graphics.window.width - graphics.ball.width) // 2
            graphics.ball.y = (graphics.window.height - graphics.ball.height) // 2
            graphics.set_listener_config()
            pause(FRAME_RATE)


if __name__ == '__main__':
    main()
