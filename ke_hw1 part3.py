# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 23:28:03 2017

@author: Kody Ellis
"""

"""
+Asks for slope and y intercept for line 1 and 2
+Program returns point of intersection if it exists
Else program says two lines dont intersect


+if two lines have they are parellel and dont intersect
"""


slope1 = raw_input("Enter the slope of the first line: ")
y_intercept1 = raw_input("Enter the y-intercept of the first line. Y-intercept is y = a2*x+b2: ")
slope2 = raw_input("Enter the slope of the second line: ")
y_intercept2 = raw_input("Enter the y-intercept of the second line. Y-intercept is y = a2*x+b2: ")

slope1 = float(slope1)
slope2 = float(slope2)


#b = y-intercept
#a = slope

if slope1 == slope2:
    print "The two lines do not have a point of intersection."
    
else:
    y_intercept1 = float(y_intercept1)
    y_intercept2 = float(y_intercept2)

    x_intersection_point = ((y_intercept2-y_intercept1) / (slope1-slope2))

    y_intersection_point = (slope1 * x_intersection_point) + y_intercept1

print "The points of intersection are: ", "(", x_intersection_point, ",", y_intersection_point, ")"
