"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Width of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        self.b_r = brick_rows
        self.b_c = brick_cols
        self.b_h = brick_height
        self.b_w = brick_width
        self.b_o = brick_offset
        self.b_s = brick_spacing
        self.ball_radius = ball_radius
        self.paddle_bottom = paddle_offset

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2,
                        y=(self.window.height-PADDLE_OFFSET))

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width-self.ball.width)//2,
                        y=(self.window.height-self.ball.height)//2)
        # Default initial velocity for the ball
        self.__dx = 0
        self.__dy = 0
        self.__listener = True
        # Initialize our mouse listeners
        onmouseclicked(self.set_ball_velocity)
        onmousemoved(self.paddle_location)

        # Draw bricks
        # brick x/y position
        self.b_y = self.b_o
        for i in range(self.b_r):
            self.b_x = 0
            for j in range(self.b_c):
                self.brick = GRect(self.b_w, self.b_h, x=self.b_x, y=self.b_y)
                self.brick.filled = True
                self.brick.fill_color = 'pink'
                self.brick.color = 'pink'
                self.b_x = self.b_x + self.b_s + self.b_w
                self.window.add(self.brick)
            self.b_y = self.b_y + self.b_h + self.b_s

    def paddle_location(self, mouse):
        # paddle with follow the mouse.x
        if mouse.x - (self.paddle.width/2) > self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        elif mouse.x < 0:
            self.paddle.x = 0
        else:
            self.paddle.x = mouse.x - (self.paddle.width / 2)

    # set the ball direction
    def set_ball_velocity(self, mouse):
        if self.__listener:
            self.ball_xy()
            self.__listener = False

    def ball_xy(self):
        self.__dx = random.randint(0, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        # 一半機率 random move x,y 往負移動
        if random.random() > 0.5:
            self.__dx = - self.__dx

    def get_ball_x(self):
        return self.__dx

    def get_ball_y(self):
        return self.__dy

    def set_ball_dx(self, new_ball_dx):
        self.__dx = new_ball_dx

    def set_ball_dy(self, new_ball_dy):
        self.__dy = new_ball_dy

    def set_listener_config(self):
        self.__listener = True
        self.__dx = 0
        self.__dy = 0

