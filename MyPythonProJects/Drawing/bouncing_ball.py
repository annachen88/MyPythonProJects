"""
File: bouncing_ball.py
Name: Anna
-------------------------
This program is to demo the bouncing ball and reduce the bounce by gravity
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3      # 球的水平速度
VY = 3      # 球的垂直速度
DELAY = 10  # 動畫停格多少毫秒(ms)
GRAVITY = 1     # 重力加速度;每一圈 while loop 垂直速度要加上的數值
SIZE = 20   # 球的直徑
REDUCE = 0.9    # 每一次反彈時,在垂直速度所剩之比例
START_X = 30    # 球的起始 x 座標
START_Y = 40    # 球的起始 y 座標
COUNT = 0


window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE)
ball.filled = True
ball.fill_color = 'black'
window.add(ball, x=START_X, y=START_Y)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(bouncing_ball)


def bouncing_ball(mouse):
    global COUNT
    # count clicked times and can't click when ball is not at the start position
    if COUNT < 3 and ball.x == START_X and ball.y == START_Y:
        call_bouncing()


def call_bouncing():
    global ball
    global COUNT
    move = VY
    go_back_stop = False
    while True:
        if go_back_stop:
            break
        else:
            ball.move(VX, move)
        if ball.y > window.height:
            # ball turn the other direction
            move = -move
            move = move * REDUCE
        else:
            move += GRAVITY
        if ball.x + ball.width >= window.width:
            # go back to the start position and stop
            ball.x = START_X
            ball.y = START_Y
            go_back_stop = True
            COUNT += 1
        pause(DELAY)


if __name__ == "__main__":
    main()
