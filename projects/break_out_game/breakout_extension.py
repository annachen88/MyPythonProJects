"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

Enhance The Brick Game with Labels (Life times and score)
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from campy.graphics.gobjects import GLabel,GRect

FRAME_RATE = 15        # 100 frames per second
NUM_LIVES = 3			# Number of attempts
score = 0
score_label = GLabel('Score: '+str(score) + '    Life: '+str(NUM_LIVES))


def main():
    graphics = BreakoutGraphics()
    total_bricks = graphics.b_r * graphics.b_c

    score_label.font = '-20'
    graphics.window.add(score_label, x=0, y=score_label.height+10)
    # Add the animation loop here!

    global NUM_LIVES
    global score
    while NUM_LIVES > 0 and total_bricks > 0:
        pause(FRAME_RATE)
        dx = graphics.get_ball_x()
        dy = graphics.get_ball_y()
        graphics.ball.move(dx, dy)
        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.set_ball_dx(-dx)
        if graphics.ball.y <= 0 or graphics.ball.y + graphics.ball.height >= graphics.window.height:
            graphics.set_ball_dy(-dy)

        #  get object
        maybe_obj_tl = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)

        if maybe_obj_tl:
            if maybe_obj_tl is graphics.paddle:
                graphics.ball_xy()
                graphics.set_ball_dx(-dx)
                graphics.set_ball_dy(-dy)

            else:
                # not including the score label
                if maybe_obj_tl is not score_label:
                    graphics.ball_xy()
                    graphics.window.remove(maybe_obj_tl)
                    total_bricks -= 1
                    score += 10

        # over the bottom
        if graphics.ball.y + graphics.ball_radius*2 >= graphics.window.height or graphics.ball.y == graphics.window.height:
            NUM_LIVES -= 1
            # graphics.ball.move(dx, dy)
            graphics.ball.x = (graphics.window.width - graphics.ball.width) // 2
            graphics.ball.y = (graphics.window.height - graphics.ball.height) // 2
            graphics.set_listener_config()
            pause(FRAME_RATE)
        score_label.text = 'Score: ' + str(score)+'  Life: '+str(NUM_LIVES)

    # ending scene
    ending = GRect(graphics.window.width, graphics.window.height)
    ending.filled = True
    ending.fill_color = 'grey'
    graphics.window.add(ending, x=-1, y=-1)
    ending_label = GLabel('Score: '+str(score))
    ending_label.font = '-20'
    graphics.window.add(ending_label, x=(graphics.window.width - score_label.width)-score_label.width,
                        y=(graphics.window.height + score_label.height)//2)


if __name__ == '__main__':
    main()
