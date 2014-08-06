from SimpleCV import *
from pygame import error as pg_err #just so pygame error is not invoked
from time import sleep
import sys

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
    set = list(ln_set)
    start_points = line_points(line)
    lowest_dist = None
    current_index = None
    closest_lines = []
    for l in set:						#Closest distance from START point of input line to another point of an another line.
        if round(l.angle()) == round(line.angle()):  #Should test rounded angle values on Triangles
            if start_points != line_points(l):
                current_points = line_points(l)
                current_dist = min(dist((start_points[0], current_points[0])), dist((start_points[0], current_points[1]))) #1st element of start_points
                if lowest_dist == None:         #This should only happen ONCE
                    lowest_dist = current_dist
                if current_dist < lowest_dist and current_dist > 0:
                    lowest_dist = current_dist
                    current_index = set.index(l)
	
    closest_lines.append(current_index)
	
    lowest_dist = None	#Reset variables
    current_index = None
    for l in set:						#Closest distance from END point of input line to another point of an another line.
        if round(l.angle()) == round(line.angle()):
            if start_points != line_points(l):
                current_points = line_points(l)
                current_dist = min(dist((start_points[1], current_points[0])), dist((start_points[1], current_points[1]))) #2nd element of start_points
                if lowest_dist == None:         #This should only happen ONCE
                    lowest_dist = current_dist
                if current_dist < lowest_dist and current_dist > 0:
                    lowest_dist = current_dist
                    current_index = set.index(l)
                    
    if current_index not in closest_lines:
        closes_lines.append(current_index)
        return closest_lines
    else:
        print "Input line is paired."
##        print "Input Line Index:", set.index(line)
        closest_lines.append(None)
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
    
    

###------------Fundamentals------------###
img_src = "test5.jpg"
img = Image(img_src)
res = img.size()
lines = img.findLines() 
ppi = round(ppi(15.6))
#------------END Fundamentals------------###
print nearest_line(lines[0], lines)
                  
##for l in lines:
##    print "Index:", lines.index(l), line_points(l)
##    print round(pixel_inch(l.length(), ppi), 2), "inches"
##    print l.length(), "pixels"
##    print l.angle(), "degrees"
##    print ""

        
##try:
##    while disp.isNotDone():
##        lines.draw(autocolor = True, width = 2) #alternate color to show detection
##        img.save(disp)
##        sleep(.01)
##
##except pg_err:
##    pass
