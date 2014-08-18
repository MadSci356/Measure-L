from SimpleCV import *
from pygame import error as pg_err #just so pygame error is not invoked
from time import sleep
import sys
##from webcolors import rgb_to_name

def line_points(Line):
    """Input: Line Object (not line feature "set")
    Returns a tuple of two tuples with the two endpoints of the line segment.
    """
    points = Line.points    # [(x1, y1), (x1, y1), (x2, y2), (x2, y2)]
    return points[0], points[2]


def pixel_inch(pixels, ppi):
    """Converts pixels to inches using the given ppi"""
    return pixels / float(ppi)

def ppi(screen_diagonal):    
    from ctypes import windll
    user32 = windll.user32
    screen_res = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    diagonal_px = ((screen_res[0]**2 + screen_res[1]**2)**0.5)
	
    return (diagonal_px / screen_diagonal)

def dist((p1, p2)):
    """Input: Tuple of two tuples
    Returns Distance between the two points in pixels"""
    x_diff = abs(p1[0] - p2[0])
    y_diff = abs(p1[1] - p2[1])
    return (x_diff**2 + y_diff**2)**0.5

def nearest_line(line, ln_set): 
    dup_set = list(ln_set)
    start_points = line_points(line)
    lowest_dist = None
    current_index = -100
    closest_lines = []
    for l in dup_set:	    #Closest distance from START point of input line to another point of an another line.
        if round(l.angle()) == round(line.angle()):  #Should test rounded angle values on Triangles
            if start_points != line_points(l):
                current_points = line_points(l)
                current_dist = min(dist((start_points[0], current_points[0])), dist((start_points[0], current_points[1]))) #1st element of start_points
                if lowest_dist == None:         #This should only happen ONCE
                    lowest_dist = current_dist
                    current_index = dup_set.index(l)
                if current_dist < lowest_dist and current_dist > 0:
                    lowest_dist = current_dist
                    current_index = dup_set.index(l)

    if current_index == -100:
        print "Error: No line Found."
        print "Input Line Index:", dup_set.index(line)

    closest_lines.append(current_index)
	
    lowest_dist = None	#Reset variables
    current_index = -100
    for l in dup_set:	    #Closest distance from END point of input line to another point of an another line.
        if round(l.angle()) == round(line.angle()):
            if start_points != line_points(l):
                current_points = line_points(l)
                current_dist = min(dist((start_points[1], current_points[0])), dist((start_points[1], current_points[1]))) #2nd element of start_points
                if lowest_dist == None:         #This should only happen ONCE
                    lowest_dist = current_dist
                    current_index = dup_set.index(l)
                if current_dist < lowest_dist and current_dist > 0:
                    lowest_dist = current_dist
                    current_index = dup_set.index(l)
                    
    if current_index not in closest_lines:
        closest_lines.append(current_index)
        return closest_lines
    else:
        print "Only one line found" 
        print "Input Line Index:", dup_set.index(line)
##        closest_lines.append(None)
##        print "Current Output:", closest_lines
        return closest_lines
    	

def group_lines(line_set):
    set = list(line_set)	
	
def relative_position(line1, line2):
    pt1 = line_points(line1)
    pt2 = line_points(line1)
    x1_diff= pt1[0][0] - pt2[0][0]  #diff of start x points
    y1_diff = pt1[0][1] - pt2[0][1] #diff of start y points
    x2_diff = pt1[1][0] - pt2[1][0]  #diff of end x points
    y2_diff = pt1[1][1] - pt2 [1][1] #diff of end y points
    
def good_random_color(n):
    """Input n: Number of desired colors"
    Returns: A list of n tuples containing a RGB tuple and its name
    Output: [((R, G, B), "Color's Name"), ...]
    ****R, G, and B are integers****
    """
    
##    BLUE = (0, 0, 255), "Blue"
##    ORANGE = (255, 165, 0), "Orange"  #willl confuse with Lego orange

##  Discarded because of similarity to Extended Colors
##    IVORY = (255, 255, 240), "Ivory"
##    BEIGE = (245, 245, 220), "Beige"
##    WHEAT = (245, 222, 179), "Wheat"
##    ROYALBLUE = (8, 76, 158), 
##    MEDIUMBLUE = (0, 0, 205)
##    AQUAMARINE = (127, 255, 212), "Aquamarine"
##    PLUM = (132, 49, 121), "Plum"
##    INDIGO = (75, 0, 130)
##    FUCHSIA = (255, 119, 255), "Fuchsia"
##    CRIMSON = (220, 20, 60)
    
    YELLOW = (255, 255, 0), "Yellow" 
    RED = (255, 0, 0), "Red"
    LEGO_BLUE = (0,50,150), "Lego Blue" 
    LEGO_ORANGE = (255,150,40), "Lego Orange"
    VIOLET = (181, 126, 220), "Violet"
    GREEN = (0, 128, 0), "Green"
    GRAY = (128, 128, 128), "Gray"

    #Extended Colors
    TAN = (210, 180, 140), "Tan"
    KHAKI = (195, 176, 145), "Khaki"
    SILVER = (192, 192, 192), "Silver"
    CHARCOAL = (70, 70, 70), "Charcoal"
    NAVYBLUE = (0, 0, 128), "Navy (Dark) Blue." 
    AZURE = (0, 127, 255), "Azure (Blue)"
    CYAN = (0, 255, 255), "Cyan"
    TEAL = (0, 128, 128), "Teal (Greenish Blue)"
    FORESTGREEN = (34, 139, 34), "Forest Green"
    OLIVE = (128, 128, 0), "Olive"
    LIME = (191, 255, 0), "Lime"
    GOLD = (255, 215, 0), "Gold"
    SALMON = (250, 128, 114), "Salmon"
    HOTPINK = (252, 15, 192), "Hot Pink"
    PUCE = (204, 136, 153), "Puce (Dark Pink)"
    MAROON = (128, 0, 0), "Maroon"
    
    my_colorlist = [YELLOW, RED, LEGO_BLUE,
                    LEGO_ORANGE, VIOLET, GREEN,
                    GRAY, TAN, KHAKI, SILVER,
                    CHARCOAL, NAVYBLUE, AZURE, CYAN,
                    TEAL, FORESTGREEN, OLIVE, LIME,
                    GOLD, SALMON, HOTPINK, PUCE,
                    MAROON]
                    
    from random import choice
    color_set = list(my_colorlist)
    prev = choice(color_set)
    random_color = [prev]
    for i in range(n-1):
        same = True
        while same:
            next = choice(color_set)
            if next != prev:
                same = False        
        random_color.append(next)
        prev = next
    return random_color                  
        

###------------Fundamentals------------###
img_src = "test6.jpg"
img = Image(img_src).erode()
res = img.size()
lines = img.findLines() 
ppi = round(ppi(15.6))
drawing_1 = img.dl()
drawing_1.setFontSize(35)
rand_color = good_random_color(len(lines)) #color chosen outside loop  
#------------END Fundamentals------------###
    
##print nearest_line(lines[7], lines)            

for line_and_color in zip(lines, rand_color): #[line, ((color tuple), "color name")]
    print "Index:", lines.index(line_and_color[0]), line_points(line_and_color[0])
    print "Color:", line_and_color[1][1]
    print round(pixel_inch(line_and_color[0].length(), ppi), 2), "inches"
    print line_and_color[0].length(), "pixels"
    print line_and_color[0].angle(), "degrees"
    print ""

##try:
##    disp = Display(resolution = res)
##    while disp.isNotDone():
##        mouse_pos = str((disp.mouseX, disp.mouseY))
##        drawing_1.ezViewText(mouse_pos, (0,0))
##        for feature in zip(lines, rand_color):#[line, ((color tuple), "color name")]
##            feature[0].draw(color=feature[1][0], width = 3)
##        img.save(disp)
##        sleep(.01)
##
##except pg_err:
##    pass
