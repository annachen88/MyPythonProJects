"""
File: my_drawing.py
Name: Anna
----------------------
Title : The Powerpuff Girl
The Powerpuff Girl is one of my favorite cartoon of my childhood
"""

from campy.graphics.gobjects import GOval, GRect, GLabel,GPolygon
from campy.graphics.gwindow import GWindow
window = GWindow(width=1000, height=600, title='The Powerpuff Girl')


def main():
    face()
    left_eye()
    right_eye()
    mouth()
    hair()
    bang()
    label()


def label():
    power_puff = GLabel("The Powerpuff Girl", x=600, y=300)
    power_puff.font = 'Helvetica-50-bold'
    power_puff.color = '#ff6600'
    window.add(power_puff)


def face():
    face_ob = GOval(435, 379, x=109, y=121)
    face_ob.filled = True
    face_ob.fill_color = '#f4cdb0'
    window.add(face_ob)


def hair():
    hair_1 = GOval(131, 114, x=44, y=125)
    hair_1.filled = True
    hair_1.fill_color = 'black'
    window.add(hair_1)
    hair_2 = GOval(131, 87, x=16, y=197)
    hair_2.filled = True
    hair_2.fill_color = 'black'
    window.add(hair_2)
    hair_3 = GOval(131, 114, x=476, y=105)
    hair_3.filled = True
    hair_3.fill_color = 'black'
    window.add(hair_3)
    hair_4 = GOval(131, 87, x=436, y=97)
    hair_4.filled = True
    hair_4.fill_color = 'black'
    window.add(hair_4)


def bang():
    bang_1 = GPolygon()
    bang_1.add_vertex((241, 132))
    bang_1.add_vertex((334, 95))
    bang_1.add_vertex((432, 107))
    bang_1.add_vertex((517, 162))
    bang_1.add_vertex((199, 190))
    bang_1.add_vertex((133, 190))
    bang_1.add_vertex((190, 132))
    bang_1.add_vertex((243, 94))
    bang_1.add_vertex((334, 95))
    bang_1.add_vertex((334, 95))
    bang_1.filled = True
    bang_1.filled = 'black'
    window.add(bang_1)


def mouth():
    mouth_back = GOval(50, 55, x=318, y=373)
    mouth_back.filled = True
    mouth_back.fill_color = 'black'
    window.add(mouth_back)
    mouth_down = GOval(53, 47, x=315, y=371)
    mouth_down.filled = True
    mouth_down.fill_color = '#f4cdb0'
    mouth_down.color = '#f4cdb0'
    window.add(mouth_down)


def right_eye():
    r_eye = GOval(189, 206, x=346, y=186)
    r_eye.filled = True
    r_eye.fill_color = 'white'
    window.add(r_eye)
    r_eye_1 = GOval(155, 170, x=345, y=210)
    r_eye_1.filled = True
    r_eye_1.fill_color =  '#a8dffe'  #'#edd632'
    window.add(r_eye_1)
    r_eye_2 = GOval(123, 151, x=346, y=217)
    r_eye_2.filled = True
    r_eye_2.fill_color = 'black'
    window.add(r_eye_2)
    r_eye_3 = GOval(56, 59, x=362, y=240)
    r_eye_3.filled = True
    r_eye_3.fill_color = 'white'
    window.add(r_eye_3)
    r_eye_4 = GOval(35, 37, x=420, y=266)
    r_eye_4.filled = True
    r_eye_4.fill_color = 'white'
    window.add(r_eye_4)
    r_eye_4 = GOval(35, 37, x=420, y=266)
    r_eye_4.filled = True
    r_eye_4.fill_color = 'white'
    window.add(r_eye_4)
    r_eye_5 = GOval(31, 33, x=395, y=300)
    r_eye_5.filled = True
    r_eye_5.fill_color = 'white'
    window.add(r_eye_5)


def left_eye():
    l_eye = GOval(180, 205, x=120, y=228)
    l_eye.filled = True
    l_eye.fill_color = 'white'
    window.add(l_eye)
    l_eye_1 = GOval(151, 177, x=148, y=239)
    l_eye_1.filled = True
    l_eye_1.fill_color = '#a8dffe' #'#edd632'
    window.add(l_eye_1)
    l_eye_2 = GOval(123, 151, x=175, y=248)
    l_eye_2.filled = True
    l_eye_2.fill_color = 'black'
    window.add(l_eye_2)
    l_eye_3 = GOval(56, 59, x=217, y=266)
    l_eye_3.filled = True
    l_eye_3.fill_color = 'white'
    window.add(l_eye_3)
    l_eye_4 = GOval(35, 37, x=197, y=320)
    l_eye_4.filled = True
    l_eye_4.fill_color = 'white'
    window.add(l_eye_4)
    l_eye_5 = GOval(31, 33, x=235, y=329)
    l_eye_5.filled = True
    l_eye_5.fill_color = 'white'
    window.add(l_eye_5)


if __name__ == '__main__':
    main()
