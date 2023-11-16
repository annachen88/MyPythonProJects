"""
File: babygraphics.py
Name: Anna
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    return GRAPH_MARGIN_SIZE + (width // len(YEARS) * year_index)


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.create_line(0, GRAPH_MARGIN_SIZE, CANVAS_WIDTH, GRAPH_MARGIN_SIZE, width=LINE_WIDTH, fill='black')
    canvas.create_line(0, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE, CANVAS_WIDTH, CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH, fill='black')
    for i in range(len(YEARS)):
        canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), GRAPH_MARGIN_SIZE,
                           get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT,
                           width=LINE_WIDTH, fill='black')
        # print(get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT,YEARS[i])
        canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE, text=YEARS[i]
                           , anchor=tkinter.NW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.

    name_data = {'Kylie': {'2010': '57', '2000': '104'},
    'Nick': {'2010': '37'},
    'Kate': {'2010': '208', '2000': '108'},
    'Sammy': {'1990': '90'}}
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    color_count = 0
    sample_size = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
    for lookup_name in lookup_names:
        color_count = color_count % len(COLORS)
        color = COLORS[color_count]
        color_count += 1
        if lookup_name in name_data:
            for i in range(len(YEARS)-1):
                if str(YEARS[i]) in name_data[lookup_name]:
                    text = name_data[lookup_name][str(YEARS[i])]
                    if str(YEARS[i+1]) in name_data[lookup_name]:
                        # get line -> x1,y1 x2,y2
                        y1_line = GRAPH_MARGIN_SIZE+int(int(name_data[lookup_name][str(YEARS[i])])/1000 * sample_size)
                        y2_line = GRAPH_MARGIN_SIZE+int(int(name_data[lookup_name][str(YEARS[i+1])])/1000 * sample_size)
                        text = name_data[lookup_name][str(YEARS[i])]
                        # print('1', get_x_coordinate(CANVAS_WIDTH, i), name_data[lookup_name][str(YEARS[i])],
                        #       get_x_coordinate(CANVAS_WIDTH, i + 1), name_data[lookup_name][str(YEARS[i+1])])
                        text2 = name_data[lookup_name][str(YEARS[i+1])]
                    else:
                        y1_line = GRAPH_MARGIN_SIZE+int(int(name_data[lookup_name][str(YEARS[i])])/1000 * sample_size)
                        y2_line = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE

                        # print('2', get_x_coordinate(CANVAS_WIDTH, i), name_data[lookup_name][str(YEARS[i])],
                        #       get_x_coordinate(CANVAS_WIDTH, i + 1), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
                        text2 = '*'

                else:
                    text = '*'
                    if str(YEARS[i + 1]) in name_data[lookup_name]:
                        y1_line = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                        y2_line = GRAPH_MARGIN_SIZE+int(int(name_data[lookup_name][str(YEARS[i + 1])])/1000 * sample_size)
                        # print('3', get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                        #       get_x_coordinate(CANVAS_WIDTH, i + 1), name_data[lookup_name][str(YEARS[i + 1])])
                        text2 = name_data[lookup_name][str(YEARS[i + 1])]
                    else:
                        # x1_line = get_x_coordinate(CANVAS_WIDTH, i)
                        y1_line = CANVAS_HEIGHT - GRAPH_MARGIN_SIZE
                        # x2_line = get_x_coordinate(CANVAS_WIDTH, i + 1)
                        y2_line = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
                        # print('4', get_x_coordinate(CANVAS_WIDTH, i), CANVAS_HEIGHT - GRAPH_MARGIN_SIZE,
                        #       get_x_coordinate(CANVAS_WIDTH, i + 1), CANVAS_HEIGHT-GRAPH_MARGIN_SIZE)
                        text2 = '*'
                # draw the line
                canvas.create_line(get_x_coordinate(CANVAS_WIDTH, i), y1_line, get_x_coordinate(CANVAS_WIDTH, i + 1),
                                   y2_line, width=LINE_WIDTH, fill=color)
                # add text
                canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i) + TEXT_DX, y1_line, text=lookup_name + ' ' + text,
                                   anchor=tkinter.SW,fill=color)
            # last one text
            canvas.create_text(get_x_coordinate(CANVAS_WIDTH, i+1) + TEXT_DX, y2_line, text=lookup_name + ' ' + text2,
                               anchor=tkinter.SW, fill=color)


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
