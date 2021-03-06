# -*- coding: utf-8 -*-
"""
Created on Fri Nov 03 16:15:47 2017

@author: Kody Ellis
"""

#I believe this code is better than the other version of lab7 however this does fulfill the lab direction 
#requirements 100%. So I might be penalized if I turned this version of the lab in.
import numpy
#There's no need to preiniatialize empty array like humid or wind_speed

#Field makes it traverse the main data fields of the weather file provided. It provides a clean, clear way to get form data.
#aWeaherData and aDate do not HAVE to be default parameters but I made them default because
#in a test case they are the values that would most likely be entered anyway.
def weatherStats(field,aWeatherFile = "weather_data.csv", aDate = '11/3/2017', ):
    """"This opens up a designated file that should be weather data.csv
    The program then starts to read the file. For every line in the file, if 
    it starts with a '#' or a non-numerical character the program skips it.
    
    
    If the file has a numerical chracter, it starts to append data to a list 
    using the split() function. The field parameter is for getting 
    certain types of data, as each increase in the field starting from 0 will
    return a new field of data. 
    
    
    For example is field = 2 then the field will
    return all data for relative humidity.
    """
    
    file_connector = open(aWeatherFile, "r")
    field_data = []
    #prints baromeric pressure
    for line in file_connector:
        if line[0] == "#" or (not line [0].isdigit()) :
            pass
        else:
            #only gets items from date
            if line.split()[0] == aDate:
                #split(",")[2] takes relative humidity
                field_data.append(float(line.split()[1].split(",")[field]))
    file_connector.close()
    return field_data

barometric_p = min(weatherStats(1))
humid = max(weatherStats(2))
temperature = numpy.mean(weatherStats(3))
wind_direction = numpy.median(weatherStats(4))
wind_speed = numpy.mean(weatherStats(5))

print "Barometric Pressure:", barometric_p
print "Relative Humidity:", humid
print "Temperature:",temperature
print "Wind Direction:", wind_direction
print "Wind Speed:", wind_speed

        
        

