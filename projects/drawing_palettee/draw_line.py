"""
File: draw_line.py
Name: Anna
-------------------------
This program is to draw the line,first time draw the circle second draw the line, continue...
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10
ball_track = GOval(SIZE, SIZE)
window = GWindow()
even = False
start_x = 1
start_y = 1


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    global even
    global start_x
    global start_y

    if not even:
        # draw ball
        ball = GOval(SIZE, SIZE)
        ball.color = 'black'
        window.add(ball, x=mouse.x-ball.width//2, y=mouse.y-ball.height//2)
        start_x = mouse.x
        start_y = mouse.y
        even = True
    else:
        # draw line
        maybe_obj = window.get_object_at(start_x, start_y)
        window.remove(maybe_obj)
        line = GLine(start_x, start_y, mouse.x, mouse.y)
        window.add(line)
        start_x = mouse.x
        start_y = mouse.y
        even = False


if __name__ == "__main__":
    main()
